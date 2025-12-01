from sklearn.cluster import KMeans, DBSCAN
import pandas as pd
from queries import neo4j_queries, mongo_queries

def extract_wallet_features():
    """Extract features from Neo4j for each wallet"""
    query = """
    MATCH (w:Wallet)
    OPTIONAL MATCH (w)-[r]-()
    WITH w, count(r) as degree
    OPTIONAL MATCH (w)-[sent:SENT]->()
    WITH w, degree, avg(sent.value) as avg_sent, sum(sent.value) as total_sent
    RETURN w.address as address, degree, avg_sent, total_sent
    """
    results = neo4j_queries.graph.run(query).data()
    return pd.DataFrame(results)

def cluster_wallets(n_clusters=5):
    """Cluster wallets by behavior"""
    df = extract_wallet_features()
    df = df.fillna(0)
    
    features = df[['degree', 'avg_sent', 'total_sent']]
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(features)
    
    # Store results back in MongoDB
    for _, row in df.iterrows():
        mongo_queries.db['wallet_clusters'].update_one(
            {'address': row['address']},
            {'$set': {'cluster': int(row['cluster']), 
                      'degree': row['degree'],
                      'avg_sent': row['avg_sent']}},
            upsert=True
        )
    
    return df