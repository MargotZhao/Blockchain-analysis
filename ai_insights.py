# ai_insights.py - AI-Powered Data Explanations (Educational Only)
# Updated for OpenAI v1.0+ API
from openai import OpenAI
import config
from typing import Dict, List, Any
import json

# Initialize OpenAI client with new v1.0+ syntax
client = OpenAI(api_key=config.OPENAI_API_KEY)

# System prompt that enforces educational focus
SYSTEM_PROMPT = """You are an educational blockchain data analyst assistant. Your role is to:
1. Explain blockchain transaction data in clear, educational terms
2. Describe patterns and what they mean
3. Provide context about blockchain concepts
4. Summarize data insights

CRITICAL RULES:
- NEVER give investment advice or recommendations to buy/sell
- NEVER predict future prices or returns
- NEVER suggest financial actions
- ALWAYS include a disclaimer that this is educational only
- Focus on explaining DATA, not making predictions
- If asked for investment advice, redirect to educational explanation

Your responses should be:
- Clear and concise (2-3 paragraphs max)
- Educational and informative
- Data-focused, not speculative
- Appropriate for students learning about blockchain
"""

def explain_wallet_data(wallet_data: Dict[str, Any]) -> str:
    """
    Generate educational explanation of wallet transaction data
    
    Args:
        wallet_data: Dictionary containing wallet statistics
        
    Returns:
        Educational explanation of the data
    """
    
    try:
        # Prepare the data summary for the AI
        data_summary = f"""
        Wallet Statistics:
        - Address: {wallet_data.get('address', 'Unknown')}
        - Total Transactions: {wallet_data.get('transaction_count', 0)}
        - Total Sent: {wallet_data.get('total_sent_eth', 0)} ETH
        - Total Received: {wallet_data.get('total_received_eth', 0)} ETH
        - Net Flow: {wallet_data.get('net_flow_eth', 0)} ETH
        - Unique Counterparties: {wallet_data.get('unique_counterparties', 0)}
        """
        
        # Use new OpenAI v1.0+ API
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using GPT-4o-mini for cost efficiency
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Explain this wallet's transaction data in educational terms:\n\n{data_summary}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        
        # Add disclaimer
        disclaimer = "\n\n⚠️ Disclaimer: This is educational information only, not financial advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


def explain_high_value_transactions(transactions: List[Dict[str, Any]]) -> str:
    """
    Generate educational explanation of high-value transaction patterns
    
    Args:
        transactions: List of transaction dictionaries
        
    Returns:
        Educational explanation
    """
    
    try:
        # Summarize the transactions
        total_count = len(transactions)
        total_value = sum(tx.get('value_eth', 0) for tx in transactions)
        avg_value = total_value / total_count if total_count > 0 else 0
        
        # Get unique wallets
        unique_senders = len(set(tx.get('from', '') for tx in transactions))
        unique_receivers = len(set(tx.get('to', '') for tx in transactions))
        
        summary = f"""
        High-Value Transaction Analysis:
        - Total Transactions: {total_count}
        - Total Value: {total_value:.4f} ETH
        - Average Value: {avg_value:.4f} ETH
        - Unique Senders: {unique_senders}
        - Unique Receivers: {unique_receivers}
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Explain what these high-value transaction patterns tell us from an educational blockchain perspective:\n\n{summary}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        disclaimer = "\n\n⚠️ Disclaimer: This is educational information only, not financial advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


def explain_market_data(market_data: List[Dict[str, Any]]) -> str:
    """
    Generate educational explanation of cryptocurrency market data
    
    Args:
        market_data: List of market data dictionaries
        
    Returns:
        Educational explanation
    """
    
    try:
        # Summarize market data
        summary_lines = []
        for coin in market_data[:5]:  # Top 5 coins
            name = coin.get('name', 'Unknown')
            price = coin.get('current_price', 0)
            change_24h = coin.get('price_change_percentage_24h', 0)
            summary_lines.append(f"- {name}: ${price:,.2f} ({change_24h:+.2f}% 24h)")
        
        summary = "Current Market Snapshot:\n" + "\n".join(summary_lines)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Explain this cryptocurrency market data from an educational perspective. What do these price movements tell us about the market?\n\n{summary}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        disclaimer = "\n\n⚠️ Disclaimer: This is educational information only, not financial or investment advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


def explain_clustering_results(clustering_data: Dict[str, Any]) -> str:
    """
    Generate educational explanation of ML clustering results
    
    Args:
        clustering_data: Dictionary containing clustering results
        
    Returns:
        Educational explanation
    """
    
    try:
        summary = f"""
        Machine Learning Clustering Results:
        - Clusters Found: {clustering_data.get('clusters_found', 0)}
        - Wallets Analyzed: {clustering_data.get('wallets_clustered', 0)}
        - Cluster Distribution: {clustering_data.get('sample_clusters', {})}
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Explain what these wallet clustering results mean from a data science perspective. What patterns might these clusters represent?\n\n{summary}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        disclaimer = "\n\n⚠️ Disclaimer: This is educational information about data patterns, not financial advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


def explain_network_analysis(network_data: Dict[str, Any]) -> str:
    """
    Generate educational explanation of wallet network connections
    
    Args:
        network_data: Dictionary containing network analysis data
        
    Returns:
        Educational explanation
    """
    
    try:
        summary = f"""
        Wallet Network Analysis:
        - Wallet Address: {network_data.get('address', 'Unknown')}
        - Direct Connections: {network_data.get('direct_connections', 0)}
        - Degree Centrality: {network_data.get('degree_centrality', 0)}
        - Number of Connected Wallets: {len(network_data.get('connected_wallets', []))}
        """
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Explain what this wallet's network position tells us about its activity patterns in the blockchain ecosystem:\n\n{summary}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        disclaimer = "\n\n⚠️ Disclaimer: This is educational network analysis, not financial advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error generating explanation: {str(e)}"


# Budget-friendly alternative using GPT-3.5-turbo (even cheaper)
def explain_data_cheap(data: Any, data_type: str = "general") -> str:
    """
    Budget-friendly explanation using GPT-3.5-turbo
    
    Args:
        data: Any data to explain
        data_type: Type of data (wallet, transactions, market, etc.)
        
    Returns:
        Educational explanation
    """
    
    try:
        prompt = f"Explain this {data_type} data in simple, educational terms for a blockchain analytics student:\n\n{json.dumps(data, indent=2)[:1000]}"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        explanation = response.choices[0].message.content
        disclaimer = "\n\n⚠️ Educational information only, not financial advice."
        
        return explanation + disclaimer
        
    except Exception as e:
        return f"Error: {str(e)}"