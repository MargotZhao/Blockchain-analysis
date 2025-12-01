import requests
import time

def fetch_market_data(coins=['bitcoin', 'ethereum'], vs_currency='usd'):
    """Fetch current market data from CoinGecko"""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': vs_currency,
        'ids': ','.join(coins)
    }
    response = requests.get(url, params=params)
    time.sleep(2)  # Respect rate limit (30/min)
    return response.json()

def fetch_historical_data(coin_id, days=30):
    """Fetch historical price data"""
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {'vs_currency': 'usd', 'days': days}
    response = requests.get(url, params=params)
    time.sleep(2)
    return response.json()