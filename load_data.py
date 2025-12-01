# load_data.py
import time
from data_fetch import coingecko, etherscan
from queries import mongo_queries, neo4j_queries
from datetime import datetime

# Sample wallet addresses for testing
SAMPLE_WALLETS = [
    '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',  # Binance Hot Wallet
    '0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503',  # Binance Cold Wallet
    '0x8894E0a0c962CB723c1976a4421c95949bE2D4E3',  # Another active wallet
]

def fetch_and_store_market_data():
    """Fetch market data from CoinGecko and store in MongoDB"""
    print("Fetching market data from CoinGecko...")
    
    coins = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana']
    market_data = coingecko.fetch_market_data(coins)
    
    # Add timestamp
    for coin in market_data:
        coin['fetched_at'] = datetime.now()
    
    print(f"Retrieved data for {len(market_data)} coins")
    mongo_queries.insert_market_data(market_data)
    print("Market data stored in MongoDB ✓")
    
    return market_data

def fetch_and_store_transactions():
    """Fetch transactions from Etherscan and store in both databases"""
    print("\nFetching transactions from Etherscan...")
    
    all_transactions = []
    
    for wallet in SAMPLE_WALLETS:
        print(f"Fetching transactions for {wallet[:10]}...")
        
        txs = etherscan.fetch_wallet_transactions(
            wallet, 
            page=1, 
            offset=100
        )
        
        if not txs:
            print(f"  ⚠ No transactions returned for {wallet[:10]}")
            continue
        
        # Clean and prepare data
        for tx in txs:
            try:
                # Handle large Wei values - store as string to avoid overflow
                value_wei_str = str(tx.get('value', '0'))
                value_eth = float(value_wei_str) / 1e18 if value_wei_str.isdigit() else 0
                
                cleaned_tx = {
                    'hash': tx.get('hash'),
                    'from': tx.get('from', '').lower(),
                    'to': tx.get('to', '').lower(),
                    'value_wei': value_wei_str,  # Store as STRING to avoid overflow
                    'value_eth': value_eth,       # Float is fine
                    'timestamp': datetime.fromtimestamp(int(tx.get('timeStamp', 0))),
                    'block_number': int(tx.get('blockNumber', 0)),
                    'gas_used': int(tx.get('gasUsed', 0)),
                    'gas_price': str(tx.get('gasPrice', '0')),  # Store as string too
                }
                all_transactions.append(cleaned_tx)
                
            except (ValueError, TypeError, KeyError) as e:
                print(f"  Skipping transaction due to error: {e}")
                continue
        
        time.sleep(2)  # Respect API rate limits
    
    print(f"\n{'='*60}")
    print(f"Total processed transactions: {len(all_transactions)}")
    print(f"{'='*60}")
    
    if all_transactions:
        # Show sample
        if len(all_transactions) > 0:
            sample = all_transactions[0]
            print(f"\nSample transaction:")
            print(f"  From: {sample['from'][:10]}...")
            print(f"  To: {sample['to'][:10]}...")
            print(f"  Value: {sample['value_eth']:.6f} ETH")
        
        mongo_queries.insert_transactions(all_transactions)
        print("\n✓ Transactions stored in MongoDB")
        
        print("\nCreating wallet graph in Neo4j...")
        neo4j_queries.create_wallet_nodes_and_transactions(all_transactions)
        print("✓ Graph created in Neo4j")
    else:
        print("\n⚠ No transactions to store!")
    
    return all_transactions

def main():
    print("=" * 60)
    print("CryptoGraph Data Loading Script")
    print("=" * 60)
    
    # Fetch and store data
    market_data = fetch_and_store_market_data()
    transactions = fetch_and_store_transactions()
    
    print("\n" + "=" * 60)
    print("Data Loading Complete!")
    print("=" * 60)
    print(f"✓ {len(market_data)} coins in MongoDB")
    print(f"✓ {len(transactions)} transactions in MongoDB")
    print(f"✓ Wallet graph created in Neo4j")
    print("\nReady to run queries and Flask app!")

if __name__ == "__main__":
    main()