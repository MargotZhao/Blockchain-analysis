# app.py - COMPLETE VERSION WITH ALL ENDPOINTS
from flask import Flask, jsonify, request, render_template
from queries import mongo_queries, neo4j_queries
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)