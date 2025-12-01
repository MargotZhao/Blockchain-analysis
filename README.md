# CryptoGraph: Blockchain Analytics Platform with MetaMask Integration

A comprehensive NoSQL-based blockchain analytics application that combines MongoDB, Neo4j, machine learning, and Web3 wallet connectivity to analyze cryptocurrency transactions and market trends.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green.svg)
![Neo4j](https://img.shields.io/badge/Neo4j-Latest-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)
![MetaMask](https://img.shields.io/badge/MetaMask-Integrated-orange.svg)
![License](https://img.shields.io/badge/license-Educational-orange.svg)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [What's New: MetaMask Integration](#-whats-new-metamask-integration)
- [Architecture](#%EF%B8%8F-architecture)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Database Setup](#%EF%B8%8F-database-setup)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [MetaMask Features Guide](#-metamask-features-guide)
- [Query Examples](#-query-examples)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Academic Context](#-academic-context)

---

## 🎯 Project Overview

CryptoGraph is a full-stack data science application built for DS5760 NoSQL course at Vanderbilt University. It demonstrates the integration of multiple NoSQL databases (MongoDB for document storage, Neo4j for graph analytics) with real-world blockchain data from public APIs, enhanced with **Web3 wallet connectivity via MetaMask**.

**Key Objectives:**
- Fetch and store real-time cryptocurrency market data
- Analyze Ethereum blockchain transactions
- Visualize wallet transaction networks
- Apply machine learning clustering to detect transaction patterns
- Provide a REST API and interactive web interface
- **NEW: Connect users' Ethereum wallets for personalized analytics**

---

## ✨ Features

### Data Collection
- ✅ Real-time cryptocurrency prices from CoinGecko API
- ✅ Ethereum blockchain transactions from Etherscan API V2
- ✅ Support for multiple wallet addresses
- ✅ Automatic data cleaning and normalization

### NoSQL Databases
- ✅ **MongoDB**: Stores transactions, market data, and ML results
- ✅ **Neo4j**: Graph database for wallet relationship analysis
- ✅ Both databases running in Docker containers

### Analytics Queries (7+ Implemented)
1. Retrieve high-value transactions (>X ETH)
2. Get all transactions for a specific wallet
3. Aggregate transaction volume by day
4. Identify top 10 most active wallets
5. Find shortest path between wallet addresses (Neo4j)
6. Detect wallet "hubs" with high connectivity
7. Join market price data with transaction history

### Web Application
- ✅ Flask-based REST API
- ✅ Interactive web dashboard with modern UI
- ✅ Wallet search functionality
- ✅ Pre-built query buttons
- ✅ JSON result display
- ✅ **NEW: MetaMask wallet connection**
- ✅ **NEW: Personalized analytics dashboard**
- ✅ **NEW: Transaction data export**

### Machine Learning
- ✅ Unsupervised clustering (K-Means/DBSCAN)
- ✅ Feature extraction from Neo4j graph metrics
- ✅ Anomaly detection for suspicious wallets

### **🆕 MetaMask Integration**
- ✅ Connect Ethereum wallets via MetaMask
- ✅ Real-time ETH balance display
- ✅ Network detection (Mainnet/Testnet)
- ✅ Personalized transaction analytics
- ✅ Export wallet transaction history
- ✅ View wallet network connections
- ✅ Beautiful stat cards showing wallet activity

---

## 🆕 What's New: MetaMask Integration

### User Benefits
**Before:** Generic analytics for sample wallets only  
**After:** Personalized analytics for YOUR actual Ethereum wallet

### New Capabilities
1. **Wallet Connection**: One-click MetaMask integration
2. **Live Balance**: Real-time ETH balance from blockchain
3. **Personalized Stats**: See YOUR transaction history, volume, and connections
4. **Data Export**: Download your transaction data as JSON
5. **Network Analysis**: Visualize YOUR wallet's connections
6. **Responsive UI**: Beautiful gradient design with stat cards

### Technical Implementation
- Web3 JavaScript integration
- MetaMask browser extension detection
- Ethereum JSON-RPC API calls
- MongoDB queries filtered by user address
- Neo4j graph queries for user's network

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              Web Browser + MetaMask                 │
│            (http://localhost:5000)                  │
└───────────────────┬─────────────────────────────────┘
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
┌──────────────────┐   ┌──────────────────┐
│   MetaMask       │   │  Flask Web App   │
│  (Web3 Provider) │   │  • REST API      │
│  • ETH Balance   │   │  • HTML/CSS/JS   │
│  • Network Info  │   │  • User Queries  │
└──────────────────┘   └────────┬─────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
         ┌──────────────────┐    ┌──────────────────────┐
         │    MongoDB       │    │      Neo4j           │
         │  (Port 27017)    │    │   (Port 7474/7687)   │
         │                  │    │                      │
         │ • Transactions   │    │ • Wallet Nodes       │
         │ • Market Data    │    │ • Transaction Edges  │
         │ • ML Results     │    │ • Graph Analytics    │
         └──────────────────┘    └──────────────────────┘
                    ▲                       ▲
                    │                       │
                    └──────────┬────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Data Loaders      │
                    │                     │
                    │ • CoinGecko API     │
                    │ • Etherscan API V2  │
                    └─────────────────────┘
```

---

## 🛠️ Technologies Used

### Backend
- **Python 3.12**
- **Flask** - Web framework
- **PyMongo** - MongoDB driver
- **py2neo** - Neo4j driver
- **Requests** - HTTP library for API calls
- **pandas** - Data manipulation
- **scikit-learn** - Machine learning

### Databases
- **MongoDB 7.0** - Document database
- **Neo4j Latest** - Graph database
- **Docker & Docker Compose** - Container orchestration

### APIs
- **CoinGecko API** - Cryptocurrency market data (free tier)
- **Etherscan API V2** - Ethereum blockchain data (free tier)
- **Ethereum JSON-RPC** - Direct blockchain queries via MetaMask

### Frontend
- **HTML5/CSS3**
- **Vanilla JavaScript**
- **Web3 JavaScript** (via MetaMask injection)
- **JSON** for data interchange
- **Modern CSS Gradients** for beautiful UI

### Web3 Integration
- **MetaMask Browser Extension** - Ethereum wallet
- **Web3 Provider** (window.ethereum)
- **ETH JSON-RPC Methods** - Balance, network, accounts

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- Docker Desktop
- Git (optional)
- **MetaMask browser extension** (for wallet features)

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/cryptograph.git
cd cryptograph
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\Activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install pymongo py2neo flask requests pandas scikit-learn python-dotenv
```


### Step 4: Configure API Keys

Update `config.py` with your API keys:

```python
# config.py
COINGECKO_API_KEY = "your-coingecko-key"  # Optional, free tier works
ETHERSCAN_API_KEY = "your-etherscan-key"

# MongoDB Configuration
MONGO_URI = "mongodb://admin:cryptopass123@localhost:27017/"
MONGO_DB = "cryptograph"

# Neo4j Configuration
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "cryptopass123"
```

**Get API Keys:**
- CoinGecko: Free, no registration required (30 req/min)
- Etherscan: Register at https://etherscan.io/myapikey (100k calls/day free)

### Step 5: Install MetaMask (For Wallet Features)

1. Go to https://metamask.io/download/
2. Install the browser extension (Chrome, Firefox, Edge, Brave)
3. Create a new wallet or import existing one
4. Make sure you're on **Ethereum Mainnet**

---

## 🗄️ Database Setup

### Start Databases with Docker

```bash
# Start both databases
docker-compose up -d

# Verify they're running
docker-compose ps

# Expected output:
# NAME                    STATUS         PORTS
# cryptograph-mongodb     Up            0.0.0.0:27017->27017/tcp
# cryptograph-neo4j       Up            0.0.0.0:7474->7474/tcp, 0.0.0.0:7687->7687/tcp
```

### Database Credentials

**MongoDB:**
- Host: `localhost:27017`
- Username: `admin`
- Password: `cryptopass123`
- Database: `cryptograph`

**Neo4j:**
- Browser: http://localhost:7474
- Bolt: `bolt://localhost:7687`
- Username: `neo4j`
- Password: `cryptopass123`

---

## 🚀 Running the Application

### 1. Load Data into Databases

```bash
# Make sure Docker containers are running
docker-compose ps

# Load cryptocurrency and transaction data
python load_data.py
```

**Expected Output:**
```
============================================================
CryptoGraph Data Loading Script
============================================================
Fetching market data from CoinGecko...
Retrieved data for 5 coins
Market data stored in MongoDB ✓

Fetching transactions from Etherscan...
✓ 293 transactions in MongoDB
✓ 133 transaction relationships in Neo4j
Ready to run queries and Flask app!
```

### 2. Test Queries (Optional)

```bash
python test_queries.py
```

### 3. Start Flask Web Application

```bash
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 4. Access the Application

Open your browser:
- **Web Dashboard:** http://localhost:5000
- **Neo4j Browser:** http://localhost:7474

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Standard Endpoints

#### 1. Get Transactions by Wallet
```http
GET /api/transactions/<wallet_address>
```

**Example:**
```
http://localhost:5000/api/transactions/0x742d35cc6634c0532925a3b844bc454e4438f44e
```

**Response:**
```json
[
  {
    "hash": "0x...",
    "from": "0x742d35cc...",
    "to": "0x47ac0fb4...",
    "value_eth": 0.001234,
    "timestamp": "2021-09-15T10:30:00",
    "block_number": 13235678
  }
]
```

#### 2. Get Top 10 Wallets
```http
GET /api/top_wallets
```

**Response:**
```json
[
  {
    "_id": "0x742d35cc6634c0532925a3b844bc454e4438f44e",
    "total_sent_eth": 150000,
    "transaction_count": 198
  }
]
```

#### 3. Get High-Value Transactions
```http
GET /api/high_value_transactions
```

Returns transactions above 0.001 ETH (top 20)

#### 4. Get Market Data
```http
GET /api/market
```

**Response:**
```json
[
  {
    "name": "Bitcoin",
    "symbol": "btc",
    "current_price": 43250.50,
    "market_cap": 846123456789,
    "price_change_percentage_24h": 2.5
  }
]
```

#### 5. Get Graph Summary
```http
GET /api/graph_summary
```

**Response:**
```json
{
  "total_wallets": 89,
  "total_transactions": 133,
  "total_volume_eth": 12.456789
}
```

#### 6. Find Shortest Path
```http
GET /api/shortest_path/<address1>/<address2>
```

#### 7. Run ML Clustering
```http
POST /api/run_clustering
```

---

### 🆕 MetaMask-Enhanced Endpoints

#### 8. Get Wallet Comprehensive Info
```http
GET /api/wallet/<address>
```

**Purpose:** Get complete wallet analytics when user connects MetaMask

**Response:**
```json
{
  "address": "0x742d35cc...",
  "transaction_count": 293,
  "total_sent_eth": 125.4567,
  "total_received_eth": 150.2345,
  "net_flow_eth": 24.7778,
  "unique_counterparties": 42,
  "recent_transactions": [...],
  "first_seen": "2021-09-01T10:30:00",
  "last_seen": "2024-11-30T15:45:00"
}
```

#### 9. Get Wallet Network Analysis
```http
GET /api/wallet/<address>/network
```

**Purpose:** Get Neo4j graph connections for user's wallet

**Response:**
```json
{
  "address": "0x742d35cc...",
  "direct_connections": 15,
  "degree_centrality": 28,
  "connected_wallets": [
    {
      "connected_wallet": "0x47ac0fb4...",
      "transaction_count": 5,
      "total_volume": 2.456
    }
  ]
}
```

#### 10. Export Wallet Data
```http
GET /api/wallet/<address>/export
```

**Purpose:** Download complete transaction history as JSON

**Response:**
```json
{
  "wallet": "0x742d35cc...",
  "export_date": "2024-11-30T12:00:00",
  "transaction_count": 293,
  "transactions": [...]
}
```

---

## 🦊 MetaMask Features Guide

### Connecting Your Wallet

1. **Open the application** at http://localhost:5000
2. **Click "🦊 Connect MetaMask"** in the top section
3. **MetaMask popup appears** - click "Next" then "Connect"
4. **Your wallet is now connected!**

### What You'll See When Connected

**Wallet Info Box:**
- Your shortened wallet address (e.g., 0x742d...f44e)
- Real-time ETH balance
- Current network (Ethereum Mainnet)

**Stats Cards (5 cards):**
1. **Total Sent** - Total ETH you've sent
2. **Total Received** - Total ETH you've received  
3. **Net Flow** - Net balance change (received - sent)
4. **Transactions** - Total transaction count in our database
5. **Unique Contacts** - Number of unique wallets you've interacted with

**New Buttons Appear:**
- 🔒 **My Transactions** - View your transaction history
- 🕸️ **My Network** - See your wallet connections
- 📥 **Export My Data** - Download your data as JSON

### Using the Features

#### View Your Transactions
1. Connect wallet
2. Click "🔒 My Transactions"
3. See all your transactions in JSON format

#### View Your Network
1. Connect wallet
2. Click "🕸️ My Network"
3. See your connected wallets and transaction patterns

#### Export Your Data
1. Connect wallet
2. Click "📥 Export My Data"
3. JSON file downloads automatically
4. Filename: `wallet_<your_address>_export_2024-11-30.json`

#### Refresh Data
- Click "🔄 Refresh Data" to update balance and stats

#### Disconnect
- Click "Disconnect" to remove wallet connection
- No data is stored - reconnect anytime

### Privacy & Security

✅ **What We Access:**
- Your wallet address (public)
- Your ETH balance (public blockchain data)
- Transactions in our database

❌ **What We Never Access:**
- Your private keys
- Your seed phrase
- Permission to spend funds
- Any sensitive information

🔒 **Security Notes:**
- We never ask for your seed phrase
- All data is read-only
- MetaMask handles all security
- You control all permissions

---

## 🔍 Query Examples

### MongoDB Queries

#### Query 1: High-Value Transactions
```python
from queries import mongo_queries

# Get transactions above 1 ETH
high_value = mongo_queries.get_high_value_transactions(min_eth=1.0)
print(f"Found {len(high_value)} high-value transactions")
```

#### Query 2: Wallet Transactions
```python
# Get all transactions for a specific wallet
txs = mongo_queries.get_transactions_by_wallet('0x742d35cc6634c0532925a3b844bc454e4438f44e')
```

#### Query 3: Daily Volume Aggregation
```python
# Aggregate volume by day
daily = mongo_queries.aggregate_volume_by_day()
for day in daily:
    print(f"{day['_id']}: {day['total_volume_eth']} ETH")
```

### Neo4j Queries (Cypher)

#### Query 5: Shortest Path
```cypher
MATCH path = shortestPath(
  (w1:Wallet {address: '0x742d35cc...'})-[*]-(w2:Wallet {address: '0x47ac0fb4...'})
)
RETURN path, length(path) as hops
```

#### Query 6: Find Wallet Hubs
```cypher
MATCH (w:Wallet)-[r]-()
WITH w, count(r) as connections
WHERE connections >= 10
RETURN w.address, connections
ORDER BY connections DESC
LIMIT 10
```

#### Visualize Transaction Network
```cypher
MATCH (w1:Wallet)-[r:SENT]->(w2:Wallet)
WHERE r.value > 0
RETURN w1, r, w2
LIMIT 100
```

---

## 📁 Project Structure

```
cryptograph/
├── docker-compose.yml          # Docker configuration
├── config.py                   # API keys & database connections
├── load_data.py               # Data loading script
├── test_queries.py            # Query testing script
├── app.py                     # Flask application with MetaMask endpoints
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── data_fetch/                # Data fetching modules
│   ├── __init__.py
│   ├── coingecko.py          # CoinGecko API client
│   └── etherscan.py          # Etherscan API V2 client
│
├── queries/                   # Database query modules
│   ├── __init__.py
│   ├── mongo_queries.py      # MongoDB queries
│   └── neo4j_queries.py      # Neo4j/Cypher queries
│
├── ml/                        # Machine learning modules
│   ├── __init__.py
│   └── clustering.py         # Wallet clustering algorithms
│
├── static/                    # Static files (NEW)
│   └── style.css             # MetaMask UI styling
│
└── templates/                 # HTML templates
    └── index.html            # Main dashboard with MetaMask
```

---

## 🚧 Troubleshooting

### Docker Issues

**Containers Won't Start:**
```bash
# Check Docker is running
docker --version

# Restart Docker Desktop, then:
docker-compose up -d
```

**MongoDB Connection Error:**
```bash
# Verify MongoDB is running
docker-compose ps

# Check logs
docker-compose logs mongodb
```

**Neo4j Connection Refused:**
```bash
# Restart Neo4j container
docker-compose restart neo4j

# Wait 30 seconds for Neo4j to fully start
```

### MetaMask Issues

**"MetaMask not detected":**
- Install MetaMask extension from https://metamask.io/download/
- Refresh the page after installation
- Check that MetaMask is enabled for localhost

**Connection rejected:**
- Check that you clicked "Next" then "Connect" in MetaMask popup
- Try disconnecting and reconnecting
- Make sure MetaMask is unlocked

**"No transactions found":**
- Your wallet might not be in our database
- We only have transactions for indexed wallets
- Try searching for your wallet manually first
- Or add your wallet to `load_data.py` and re-run

**Balance shows "Error":**
- Check your internet connection
- Make sure MetaMask is on Ethereum Mainnet
- Try refreshing the page

**Wrong network:**
- Click the network dropdown in MetaMask
- Select "Ethereum Mainnet"
- Page will automatically reload

### API Issues

**Etherscan API Returns 0 Transactions:**
- Verify API key is correct in `config.py`
- Check rate limits (max 5 calls/second)
- Ensure using V2 endpoint with `chainid=1`

**CoinGecko API Fails:**
- Free tier has rate limits (30 req/min)
- Wait a minute and try again
- API key is optional for basic queries

### General Issues

**Port Already in Use:**
```bash
# Stop all containers
docker-compose down

# Check what's using the port
netstat -ano | findstr :27017  # Windows
lsof -i :27017                 # Mac/Linux

# Kill the process or use different port
```

**Flask App Won't Start:**
```bash
# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install -r requirements.txt

# Check for syntax errors
python -m py_compile app.py
```

---

## 🔄 Useful Commands

### Docker Management
```bash
# Start databases
docker-compose up -d

# Stop databases
docker-compose down

# View logs
docker-compose logs -f

# Restart services
docker-compose restart

# Remove all data (CAREFUL!)
docker-compose down -v
```

### Database Access
```bash
# MongoDB shell
docker exec -it cryptograph-mongodb mongosh -u admin -p cryptopass123 --authenticationDatabase admin

# Neo4j browser
# Open: http://localhost:7474
# Username: neo4j
# Password: cryptopass123
```

### Development
```bash
# Activate virtual environment
.\venv\Scripts\Activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run Flask in debug mode
python app.py

# Test queries
python test_queries.py

# Reload data
python load_data.py
```

---

## 🎓 Academic Context

**Course:** DS5760 - NoSQL for Modern Data Science Applications  
**Institution:** Vanderbilt University Data Science Institute  
**Semester:** Fall 2024  

### Project Requirements Met

✅ **Multiple NoSQL Databases:** MongoDB (document) + Neo4j (graph)  
✅ **External Data Sources:** CoinGecko + Etherscan APIs  
✅ **7+ Queries:** Implemented across both databases  
✅ **Extension Components:**  
- REST API (10+ endpoints including MetaMask features)
- Web UI (interactive dashboard with wallet connectivity)
- ML Component (clustering analysis)
- **Web3 Integration (MetaMask wallet connection)**

### Key Learning Outcomes Demonstrated

1. **NoSQL Database Design:** Document vs. Graph databases for different use cases
2. **API Integration:** External data sources with rate limiting and error handling
3. **Full-Stack Development:** Backend (Flask/Python) + Frontend (HTML/CSS/JS)
4. **Machine Learning:** Unsupervised clustering on graph metrics
5. **Web3 Technology:** Blockchain interaction via MetaMask and Web3 APIs
6. **Docker Deployment:** Containerized database infrastructure
7. **RESTful API Design:** Clean endpoint structure with proper HTTP methods

---

## 👥 Author

**Margot Zhao**  
Data Science Institute, Vanderbilt University  
Email: [siyang.zhao@vanderbilt.edu]

---

## 📄 License

This project is created for educational purposes as part of coursework at Vanderbilt University.

---

## 🙏 Acknowledgments

- **CoinGecko** for free cryptocurrency market data API
- **Etherscan** for blockchain transaction data
- **MongoDB** and **Neo4j** for excellent NoSQL database solutions
- **MetaMask** for Web3 wallet integration
- **Vanderbilt Data Science Institute** for course instruction
- **Claude (Anthropic)** for development assistance

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review Docker logs: `docker-compose logs`
3. Verify API keys in `config.py`
4. Ensure all dependencies are installed
5. Check MetaMask is installed and connected

---

## 🔮 Future Enhancements

### Potential Features
- [ ] Real-time transaction monitoring with WebSockets
- [ ] Advanced visualizations with D3.js
- [ ] Support for multiple blockchains (Bitcoin, Polygon, BSC)
- [ ] User authentication and saved queries
- [ ] Transaction history charts and graphs
- [ ] Portfolio tracking across multiple wallets
- [ ] Price alerts and notifications
- [ ] NFT transaction analysis
- [ ] DeFi protocol tracking
- [ ] Smart contract interaction viewer

### Technical Improvements
- [ ] Redis caching layer for performance
- [ ] Pagination for large result sets
- [ ] Rate limiting for API endpoints
- [ ] Unit tests and integration tests
- [ ] CI/CD pipeline
- [ ] Production deployment guide
- [ ] API documentation with Swagger/OpenAPI
- [ ] Responsive mobile design

---

## 🌟 Project Highlights

### What Makes This Project Special

1. **Real Blockchain Data:** Not simulated - actual Ethereum transactions
2. **Multi-Database Architecture:** Demonstrates when to use document vs. graph databases
3. **Web3 Integration:** Modern blockchain connectivity via MetaMask
4. **Production-Ready Code:** Error handling, validation, proper structure
5. **User-Centric Design:** Beautiful UI with personalized analytics
6. **Educational Focus:** Clear documentation and learning objectives
7. **Scalable Design:** Easy to add new features and data sources

### Technical Achievements

- ✅ Successfully integrated 4 different APIs (CoinGecko, Etherscan, Ethereum RPC, Neo4j)
- ✅ Processed 293 real Ethereum transactions into 2 different database formats
- ✅ Built 10+ RESTful API endpoints with proper error handling
- ✅ Implemented Web3 wallet connectivity with MetaMask
- ✅ Created interactive dashboard with live blockchain data
- ✅ Deployed multi-container Docker environment
- ✅ Applied machine learning to blockchain graph data

---

## 📊 Project Metrics

**Data Volume:**
- 293 Ethereum transactions indexed
- 133 transaction relationships in graph database
- 5 cryptocurrencies tracked for market data
- 89 unique wallet addresses analyzed

**Code Metrics:**
- 10+ API endpoints
- 7+ database queries
- 3 data source integrations
- 2 NoSQL databases
- 1 machine learning algorithm

**Technical Stack:**
- Python, Flask, MongoDB, Neo4j, Docker
- HTML, CSS, JavaScript, Web3
- pandas, scikit-learn, PyMongo, py2neo

---

**⭐ If you found this project helpful, please give it a star!**

---

*Last Updated: December 2024 | Version 2.0.0 (MetaMask Edition)*
*DS5760 NoSQL Final Project | Vanderbilt University*
