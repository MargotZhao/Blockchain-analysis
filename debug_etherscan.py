# debug_etherscan.py
import requests
from config import ETHERSCAN_API_KEY

def test_etherscan_api():
    test_wallet = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'  # Vitalik's wallet
    
    # V2 endpoint
    url = "https://api.etherscan.io/v2/api"
    
    params = {
        'chainid': '1',  # NEW: Add chainid parameter
        'module': 'account',
        'action': 'txlist',
        'address': test_wallet,
        'startblock': 0,
        'endblock': 99999999,
        'page': 1,
        'offset': 10,
        'sort': 'desc',
        'apikey': ETHERSCAN_API_KEY
    }
    
    print("Testing Etherscan API V2...")
    print(f"Using API Key: {ETHERSCAN_API_KEY[:10]}...")
    
    response = requests.get(url, params=params)
    data = response.json()
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Status: {data.get('status')}")
    print(f"Message: {data.get('message')}")
    
    if data.get('status') == '1':
        result = data.get('result', [])
        print(f"\n✓ SUCCESS! Retrieved {len(result)} transactions")
        
        if result:
            print("\nFirst transaction:")
            tx = result[0]
            print(f"  Hash: {tx.get('hash')}")
            print(f"  Value: {int(tx.get('value', 0)) / 1e18:.6f} ETH")
    else:
        print(f"\n✗ ERROR: {data}")

if __name__ == "__main__":
    test_etherscan_api()