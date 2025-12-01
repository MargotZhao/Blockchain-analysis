# test_queries.py
from queries import mongo_queries, neo4j_queries

print("=" * 60)
print("Testing MongoDB Queries")
print("=" * 60)

# Query 1: High-value transactions
print("\n1. Transactions above 0.001 ETH:")
high_value = mongo_queries.get_high_value_transactions(min_eth=0.001)
print(f"Found {len(high_value)} transactions")
if high_value:
    print(f"   Top transaction: {high_value[0]['value_eth']:.6f} ETH")
    print(f"   From: {high_value[0]['from'][:15]}...")
    print(f"   To: {high_value[0]['to'][:15]}...")

# Query 2: Transactions by wallet (lowercase)
print("\n2. Transactions for Binance wallet:")
wallet = '0x742d35cc6634c0532925a3b844bc454e4438f44e'  # lowercase!
wallet_txs = mongo_queries.get_transactions_by_wallet(wallet)
print(f"Found {len(wallet_txs)} transactions")
if wallet_txs:
    print(f"   Sample: {wallet_txs[0]['value_eth']:.6f} ETH")

# Query 3: Volume by day
print("\n3. Volume aggregated by day:")
daily_volume = mongo_queries.aggregate_volume_by_day()
if daily_volume:
    for day in daily_volume[:5]:
        # Handle both possible field names
        volume = day.get('total_volume_eth', day.get('total_volume', 0))
        count = day.get('transaction_count', 0)
        print(f"   {day['_id']}: {volume:.6f} ETH ({count} txs)")
else:
    print("   No daily volume data")

# Query 4: Top wallets
print("\n4. Top 10 most active wallets:")
top_wallets = mongo_queries.get_top_wallets_by_count(limit=10)
for i, w in enumerate(top_wallets[:5], 1):
    print(f"   {i}. {w['_id'][:15]}... - {w['transaction_count']} transactions, {w.get('total_sent_eth', 0):.6f} ETH")

# Query 7: Market summary
print("\n7. Current market data:")
market = mongo_queries.get_market_summary()
for coin in market:
    change = coin.get('price_change_percentage_24h', 0)
    print(f"   {coin['name']:12s}: ${coin['current_price']:>10,.2f} ({change:>6.2f}%)")

print("\n" + "=" * 60)
print("Testing Neo4j Queries")
print("=" * 60)

# Graph summary
print("\nGraph Summary:")
summary = neo4j_queries.get_graph_summary()
if summary:
    print(f"   Total Wallets: {summary['total_wallets']}")
    print(f"   Total Transactions: {summary['total_transactions']}")
    if summary.get('total_volume_eth'):
        print(f"   Total Volume: {summary['total_volume_eth']:.6f} ETH")

# Query 6: Find hubs
print("\n6. Finding wallet hubs (min 3 connections):")
hubs = neo4j_queries.find_wallet_hubs(min_connections=3)
if hubs:
    for hub in hubs[:5]:
        print(f"   {hub['address'][:15]}... - {hub['connections']} connections")
else:
    print("   No hubs found with 3+ connections")

# Wallet stats
print("\n8. Stats for Binance wallet:")
stats = neo4j_queries.get_wallet_stats('0x742d35cc6634c0532925a3b844bc454e4438f44e')
if stats:
    sent = stats.get('total_sent_eth') or 0
    received = stats.get('total_received_eth') or 0
    print(f"   Sent: {stats['transactions_sent']} txs, {sent:.6f} ETH")
    print(f"   Received: {stats['transactions_received']} txs, {received:.6f} ETH")
else:
    print("   No stats found for this wallet")

# Connected wallets
print("\n9. Wallets connected to Binance:")
connected = neo4j_queries.get_connected_wallets('0x742d35cc6634c0532925a3b844bc454e4438f44e', limit=5)
if connected:
    for c in connected[:5]:
        print(f"   {c['address'][:15]}... - {c['connection_count']} connections")
else:
    print("   No connected wallets found")

print("\n" + "=" * 60)
print("✓ All queries completed!")
print("=" * 60)