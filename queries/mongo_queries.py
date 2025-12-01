# queries/mongo_queries.py - COMPLETE VERSION
from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['cryptograph']
transactions_collection = db['transactions']
market_collection = db['market_data']

def insert_transactions(transactions):
    """Insert transaction data into MongoDB"""
    if transactions:
        transactions_collection.insert_many(transactions)

def insert_market_data(market_data):
    """Insert market data into MongoDB"""
    if market_data:
        market_collection.insert_many(market_data)

# Query 1: Transactions above certain value
def get_high_value_transactions(min_eth=1):
    return list(transactions_collection.find({
        'value_eth': {'$gt': min_eth}
    }).sort('value_eth', -1).limit(100))

# Query 2: Transactions by wallet
def get_transactions_by_wallet(address):
    address_lower = address.lower()
    return list(transactions_collection.find({
        '$or': [
            {'from': address_lower}, 
            {'to': address_lower}
        ]
    }).limit(200))

# Query 3: Aggregate volume per day
def aggregate_volume_by_day():
    pipeline = [
        {
            '$group': {
                '_id': {
                    '$dateToString': {
                        'format': '%Y-%m-%d', 
                        'date': '$timestamp'
                    }
                },
                'total_volume_eth': {'$sum': '$value_eth'},
                'transaction_count': {'$sum': 1}
            }
        },
        {'$sort': {'_id': 1}}
    ]
    return list(transactions_collection.aggregate(pipeline))

# Query 4: Top wallets by transaction count
def get_top_wallets_by_count(limit=10):
    """Get top wallets ranked by number of transactions"""
    pipeline = [
        {
            '$group': {
                '_id': '$from',
                'total_sent_eth': {'$sum': '$value_eth'},
                'transaction_count': {'$sum': 1}
            }
        },
        {'$sort': {'transaction_count': -1}},
        {'$limit': limit}
    ]
    return list(transactions_collection.aggregate(pipeline))

# Query 4b: Top wallets by volume
def get_top_wallets_by_volume(limit=10):
    """Get top wallets ranked by total volume sent"""
    pipeline = [
        {
            '$group': {
                '_id': '$from',
                'total_sent_eth': {'$sum': '$value_eth'},
                'transaction_count': {'$sum': 1}
            }
        },
        {'$sort': {'total_sent_eth': -1}},
        {'$limit': limit}
    ]
    return list(transactions_collection.aggregate(pipeline))

# Query 7: Market data summary
def get_market_summary():
    """Get current market data summary"""
    return list(market_collection.find({}, {
        '_id': 0,
        'name': 1,
        'symbol': 1,
        'current_price': 1,
        'market_cap': 1,
        'total_volume': 1,
        'price_change_percentage_24h': 1
    }).sort('market_cap', -1))

# Additional useful queries
def get_transaction_stats():
    """Get overall transaction statistics"""
    pipeline = [
        {
            '$group': {
                '_id': None,
                'total_transactions': {'$sum': 1},
                'total_volume_eth': {'$sum': '$value_eth'},
                'avg_transaction_eth': {'$avg': '$value_eth'},
                'max_transaction_eth': {'$max': '$value_eth'},
                'min_transaction_eth': {'$min': '$value_eth'}
            }
        }
    ]
    result = list(transactions_collection.aggregate(pipeline))
    return result[0] if result else None

def search_transaction_by_hash(tx_hash):
    """Find a specific transaction by hash"""
    return transactions_collection.find_one({'hash': tx_hash})

def get_transactions_in_block(block_number):
    """Get all transactions in a specific block"""
    return list(transactions_collection.find({
        'block_number': block_number
    }).sort('timestamp', 1))

def get_recent_transactions(limit=20):
    """Get most recent transactions"""
    return list(transactions_collection.find().sort('timestamp', -1).limit(limit))