# queries/neo4j_queries.py
from py2neo import Graph, Node, Relationship
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

# Connect to Neo4j
graph = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def create_wallet_nodes_and_transactions(transactions):
    """Create wallet nodes and transaction relationships in Neo4j"""
    
    print(f"  Processing {len(transactions)} transactions for graph...")
    
    # Clear existing data (optional - comment out if you want to keep old data)
    # graph.run("MATCH (n) DETACH DELETE n")
    
    count = 0
    for tx in transactions:
        try:
            from_addr = tx.get('from', '').lower()
            to_addr = tx.get('to', '').lower()
            value_eth = tx.get('value_eth', 0)
            
            # Skip if no addresses or zero value
            if not from_addr or not to_addr or value_eth == 0:
                continue
            
            # Create or merge wallet nodes
            from_wallet = Node("Wallet", address=from_addr)
            to_wallet = Node("Wallet", address=to_addr)
            
            # Merge nodes (create if not exists, don't duplicate)
            graph.merge(from_wallet, "Wallet", "address")
            graph.merge(to_wallet, "Wallet", "address")
            
            # Create transaction relationship
            tx_rel = Relationship(
                from_wallet, 
                "SENT", 
                to_wallet,
                hash=tx.get('hash'),
                value=value_eth,
                timestamp=str(tx.get('timestamp')),
                block_number=tx.get('block_number')
            )
            
            graph.create(tx_rel)
            count += 1
            
            # Progress indicator
            if count % 50 == 0:
                print(f"    Processed {count} transactions...")
                
        except Exception as e:
            print(f"  Error creating relationship: {e}")
            continue
    
    print(f"  ✓ Created {count} transaction relationships")

def find_shortest_path(addr1, addr2):
    """Query 5: Find shortest path between two wallets"""
    addr1 = addr1.lower()
    addr2 = addr2.lower()
    
    query = """
    MATCH path = shortestPath(
        (w1:Wallet {address: $addr1})-[*]-(w2:Wallet {address: $addr2})
    )
    RETURN path, length(path) as path_length
    """
    
    result = graph.run(query, addr1=addr1, addr2=addr2).data()
    return result

def find_wallet_hubs(min_connections=10):
    """Query 6: Find wallet hubs (highly connected wallets)"""
    query = """
    MATCH (w:Wallet)-[r]-()
    WITH w, count(r) as connections
    WHERE connections >= $min_connections
    RETURN w.address as address, connections
    ORDER BY connections DESC
    LIMIT 20
    """
    
    result = graph.run(query, min_connections=min_connections).data()
    return result

def get_wallet_stats(address):
    """Get statistics for a specific wallet"""
    address = address.lower()
    
    query = """
    MATCH (w:Wallet {address: $address})
    OPTIONAL MATCH (w)-[sent:SENT]->()
    OPTIONAL MATCH (w)<-[received:SENT]-()
    RETURN 
        w.address as address,
        count(DISTINCT sent) as transactions_sent,
        count(DISTINCT received) as transactions_received,
        sum(sent.value) as total_sent_eth,
        sum(received.value) as total_received_eth
    """
    
    result = graph.run(query, address=address).data()
    return result[0] if result else None

def get_connected_wallets(address, limit=10):
    """Get wallets directly connected to this address"""
    address = address.lower()
    
    query = """
    MATCH (w:Wallet {address: $address})-[r]-(connected:Wallet)
    RETURN DISTINCT connected.address as address, count(r) as connection_count
    ORDER BY connection_count DESC
    LIMIT $limit
    """
    
    result = graph.run(query, address=address, limit=limit).data()
    return result

def get_graph_summary():
    """Get overall graph statistics"""
    query = """
    MATCH (w:Wallet)
    OPTIONAL MATCH (w)-[r:SENT]->()
    RETURN 
        count(DISTINCT w) as total_wallets,
        count(r) as total_transactions,
        sum(r.value) as total_volume_eth
    """
    
    result = graph.run(query).data()
    return result[0] if result else None

def detect_circular_transactions(max_length=5):
    """Detect circular transaction patterns (potential wash trading)"""
    query = """
    MATCH path = (w:Wallet)-[:SENT*2..5]->(w)
    WHERE length(path) <= $max_length
    RETURN w.address as wallet, length(path) as cycle_length
    LIMIT 10
    """
    
    result = graph.run(query, max_length=max_length).data()
    return result