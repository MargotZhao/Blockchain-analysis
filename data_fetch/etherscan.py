# data_fetch/etherscan.py
import requests
from config import ETHERSCAN_API_KEY
import time

def fetch_wallet_transactions(address, start_block=0, end_block=99999999, page=1, offset=100):
    """
    Fetch transactions for a wallet address using Etherscan API V2
    """
    # V2 API endpoint - ONLY CHANGE NEEDED
    url = "https://api.etherscan.io/v2/api"
    
    params = {
        'chainid': '1',  # 1 = Ethereum mainnet - NEW PARAMETER
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': start_block,
        'endblock': end_block,
        'page': page,
        'offset': offset,
        'sort': 'desc',
        'apikey': ETHERSCAN_API_KEY  # Your existing key works!
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        print(f"  API Status: {data.get('status')} - {data.get('message')}")
        
        if data.get('status') == '1':
            result = data.get('result', [])
            print(f"  Retrieved: {len(result)} transactions")
            return result
        else:
            print(f"  Error: {data.get('result', 'Unknown error')}")
            return []
            
    except Exception as e:
        print(f"  Exception: {e}")
        return []