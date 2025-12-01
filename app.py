# app.py - COMPLETE VERSION WITH METAMASK INTEGRATION
from flask import Flask, jsonify, request, render_template
from queries import mongo_queries, neo4j_queries
from bson import ObjectId
from datetime import datetime
import config
from pymongo import MongoClient
from py2neo import Graph

app = Flask(__name__)

# Database connections
mongo_client = MongoClient(config.MONGO_URI)
db = mongo_client[config.MONGO_DB]
graph = Graph(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

def serialize_doc(doc):
    """Convert MongoDB document to JSON-serializable format"""
    if isinstance(doc, dict):
        for key, value in doc.items():
            if isinstance(value, ObjectId):
                doc[key] = str(value)
            elif isinstance(value, datetime):
                doc[key] = value.isoformat()
    return doc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/transactions/<wallet>')
def get_wallet_transactions(wallet):
    txs = mongo_queries.get_transactions_by_wallet(wallet)
    # Serialize each transaction
    for tx in txs:
        serialize_doc(tx)
    return jsonify(txs)

@app.route('/api/top_wallets')
def get_top_wallets():
    wallets = mongo_queries.get_top_wallets_by_count(limit=10)
    return jsonify(wallets)

@app.route('/api/high_value_transactions')
def get_high_value():
    txs = mongo_queries.get_high_value_transactions(min_eth=0.001)
    for tx in txs:
        serialize_doc(tx)
    return jsonify(txs[:20])

@app.route('/api/market')
def get_market_data():
    data = mongo_queries.get_market_summary()
    for item in data:
        serialize_doc(item)
    return jsonify(data)

@app.route('/api/graph_summary')
def get_graph_summary():
    summary = neo4j_queries.get_graph_summary()
    return jsonify(summary if summary else {"error": "No data found"})

@app.route('/api/shortest_path/<addr1>/<addr2>')
def shortest_path(addr1, addr2):
    path = neo4j_queries.find_shortest_path(addr1, addr2)
    return jsonify(path)

@app.route('/api/wallet_stats/<address>')
def get_wallet_stats(address):
    stats = neo4j_queries.get_wallet_stats(address)
    return jsonify(stats if stats else {"error": "Wallet not found"})

@app.route('/api/run_clustering', methods=['POST'])
def run_clustering():
    try:
        # Import here to avoid errors if ml module not ready
        from ml import clustering
        result = clustering.cluster_wallets(n_clusters=5)
        
        return jsonify({
            'status': 'success',
            'message': 'Clustering completed successfully!',
            'clusters_found': int(result['cluster'].nunique()),
            'wallets_clustered': len(result),
            'sample_clusters': result.groupby('cluster').size().to_dict()
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

# ============================================================================
# NEW METAMASK ENDPOINTS
# ============================================================================

@app.route('/api/wallet/<address>')
def get_wallet_info(address):
    """Get comprehensive wallet info when user connects MetaMask"""
    
    # Validate Ethereum address format
    if not address.startswith('0x') or len(address) != 42:
        return jsonify({'error': 'Invalid Ethereum address'}), 400
    
    address = address.lower()  # Normalize to lowercase
    
    try:
        # Get transactions from MongoDB
        from_txs = list(db.transactions.find({'from': address}).sort('timestamp', -1))
        to_txs = list(db.transactions.find({'to': address}).sort('timestamp', -1))
        
        # Calculate statistics
        total_sent = sum(tx.get('value_eth', 0) for tx in from_txs)
        total_received = sum(tx.get('value_eth', 0) for tx in to_txs)
        
        # Get unique counterparties
        sent_to = set(tx['to'] for tx in from_txs if 'to' in tx)
        received_from = set(tx['from'] for tx in to_txs if 'from' in tx)
        unique_counterparties = len(sent_to.union(received_from))
        
        # Combine and sort all transactions
        all_txs = from_txs + to_txs
        all_txs.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        
        # Remove MongoDB _id for JSON serialization
        for tx in all_txs:
            if '_id' in tx:
                tx['_id'] = str(tx['_id'])
        
        return jsonify({
            'address': address,
            'transaction_count': len(all_txs),
            'total_sent_eth': round(total_sent, 6),
            'total_received_eth': round(total_received, 6),
            'net_flow_eth': round(total_received - total_sent, 6),
            'unique_counterparties': unique_counterparties,
            'recent_transactions': all_txs[:20],  # Last 20 transactions
            'first_seen': all_txs[-1].get('timestamp') if all_txs else None,
            'last_seen': all_txs[0].get('timestamp') if all_txs else None
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/wallet/<address>/network')
def get_wallet_network(address):
    """Get Neo4j network analysis for connected wallet"""
    
    if not address.startswith('0x') or len(address) != 42:
        return jsonify({'error': 'Invalid Ethereum address'}), 400
    
    address = address.lower()
    
    try:
        # Get direct connections
        query = """
        MATCH (w:Wallet {address: $address})-[r:SENT]-(other:Wallet)
        RETURN other.address as connected_wallet, 
               count(r) as transaction_count,
               sum(r.value) as total_volume
        ORDER BY transaction_count DESC
        LIMIT 20
        """
        
        result = graph.run(query, address=address).data()
        
        # Get wallet's centrality metrics
        centrality_query = """
        MATCH (w:Wallet {address: $address})-[r]-()
        RETURN count(r) as degree
        """
        
        centrality = graph.run(centrality_query, address=address).data()
        degree = centrality[0]['degree'] if centrality else 0
        
        return jsonify({
            'address': address,
            'direct_connections': len(result),
            'degree_centrality': degree,
            'connected_wallets': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/wallet/<address>/export')
def export_wallet_data(address):
    """Export wallet transaction history as JSON"""
    
    if not address.startswith('0x') or len(address) != 42:
        return jsonify({'error': 'Invalid Ethereum address'}), 400
    
    address = address.lower()
    
    try:
        # Get all transactions
        all_txs = list(db.transactions.find({
            '$or': [{'from': address}, {'to': address}]
        }).sort('timestamp', -1))
        
        # Clean for export
        for tx in all_txs:
            tx['_id'] = str(tx['_id'])
        
        return jsonify({
            'wallet': address,
            'export_date': datetime.now().isoformat(),
            'transaction_count': len(all_txs),
            'transactions': all_txs
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)