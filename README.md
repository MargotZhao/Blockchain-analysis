# CryptoGraph: Blockchain Analytics Platform

A comprehensive NoSQL-based blockchain analytics application that combines MongoDB, Neo4j, and machine learning to analyze cryptocurrency transactions and market trends.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green.svg)
![Neo4j](https://img.shields.io/badge/Neo4j-Latest-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Latest-blue.svg)
![License](https://img.shields.io/badge/license-Educational-orange.svg)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Architecture](#%EF%B8%8F-architecture)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Database Setup](#%EF%B8%8F-database-setup)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Query Examples](#-query-examples)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

CryptoGraph is a full-stack data science application built for DS5760 NoSQL course at Vanderbilt University. It demonstrates the integration of multiple NoSQL databases (MongoDB for document storage, Neo4j for graph analytics) with real-world blockchain data from public APIs.

**Key Objectives:**
- Fetch and store real-time cryptocurrency market data
- Analyze Ethereum blockchain transactions
- Visualize wallet transaction networks
- Apply machine learning clustering to detect transaction patterns
- Provide a REST API and web interface for data exploration

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
- ✅ Interactive web dashboard
- ✅ Wallet search functionality
- ✅ Pre-built query buttons
- ✅ JSON result display

### Machine Learning
- ✅ Unsupervised clustering (K-Means/DBSCAN)
- ✅ Feature extraction from Neo4j graph metrics
- ✅ Anomaly detection for suspicious wallets

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Web Browser                        │
│            (http://localhost:5000)                  │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Flask Web Application                  │
│  • REST API Endpoints                               │
│  • HTML/CSS/JavaScript Frontend                     │
└────────┬──────────────────────────┬─────────────────┘
         │                          │
         ▼                          ▼
┌──────────────────┐      ┌──────────────────────┐
│    MongoDB       │      │      Neo4j           │
│  (Port 27017)    │      │   (Port 7474/7687)   │
│                  │      │                      │
│ • Transactions   │      │ • Wallet Nodes       │
│ • Market Data    │      │ • Transaction Edges  │
│ • ML Results     │      │ • Graph Analytics    │
└──────────────────┘      └──────────────────────┘
         ▲                          ▲
         │                          │
         └──────────┬───────────────┘
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

### Frontend
- **HTML5/CSS3**
- **Vanilla JavaScript**
- **JSON** for data interchange

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- Docker Desktop
- Git (optional)

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

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys

Update `config.py` with your API keys:

```python
# config.py
COINGECKO_API_KEY = "your-coingecko-key"
ETHERSCAN_API_KEY = "your-etherscan-key"
```

**Get API Keys:**
- CoinGecko: Free, no registration required (30 req/min)
- Etherscan: Register at https://etherscan.io/myapikey (100k calls/day free)

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

### 2. Test Queries

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

### Endpoints

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

**Example:**
```
http://localhost:5000/api/shortest_path/0x742d35cc.../0x47ac0fb4...
```

#### 7. Run ML Clustering
```http
POST /api/run_clustering
```

**Response:**
```json
{
  "status": "success",
  "clusters_found": 5,
  "wallets_clustered": 89
}
```

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
├── app.py                     # Flask application
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
└── templates/                 # HTML templates
    └── index.html            # Main dashboard
```

---

## 📸 Screenshots

### Web Dashboard
![Dashboard Screenshot](screenshots/dashboard.png)

### Neo4j Graph Visualization
![Neo4j Graph](screenshots/neo4j-graph.png)

### Transaction Network
![Transaction Network](screenshots/network.png)

*Add your actual screenshots to a `screenshots/` folder in your repo*

---

## 🚧 Troubleshooting

### Docker Containers Won't Start

```bash
# Check Docker is running
docker --version

# Restart Docker Desktop, then:
docker-compose up -d
```

### MongoDB Connection Error

```bash
# Verify MongoDB is running
docker-compose ps

# Check logs
docker-compose logs mongodb
```

### Etherscan API Returns 0 Transactions

- Verify API key is correct in `config.py`
- Check rate limits (max 5 calls/second)
- Ensure using V2 endpoint with `chainid=1`

### Neo4j Connection Refused

```bash
# Restart Neo4j container
docker-compose restart neo4j

# Wait 30 seconds for Neo4j to fully start
```

### Port Already in Use

```bash
# Stop all containers
docker-compose down

# Check what's using the port
netstat -ano | findstr :27017  # Windows
lsof -i :27017                 # Mac/Linux
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

# Neo4j browser: http://localhost:7474
```

---

## 🔮 Future Enhancements

### Planned Features
- [ ] Real-time Updates: WebSocket integration for live transaction monitoring
- [ ] Advanced Visualizations: D3.js network graphs, Chart.js time series
- [ ] More ML Models: Anomaly detection, transaction classification
- [ ] Additional Blockchains: Bitcoin, Polygon, BSC support
- [ ] User Authentication: Secure login for saved queries
- [ ] Export Functionality: CSV/PDF report generation
- [ ] Caching Layer: Redis for improved performance
- [ ] Transaction Monitoring: Alert system for wallet activities

### Possible Extensions
- NFT transaction analysis
- DeFi protocol interaction tracking
- Smart contract event monitoring
- Portfolio tracking and analytics
- Cross-chain transaction correlation

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
- REST API (7+ endpoints)
- Web UI (interactive dashboard)
- ML Component (clustering analysis)

---

## 👥 Author

**Margot Zhao**  
Data Science Institute, Vanderbilt University

---

## 📄 License

This project is created for educational purposes as part of coursework at Vanderbilt University.

---

## 🙏 Acknowledgments

- **CoinGecko** for free cryptocurrency market data API
- **Etherscan** for blockchain transaction data
- **MongoDB** and **Neo4j** for excellent NoSQL database solutions
- **Vanderbilt Data Science Institute** for course instruction

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review Docker logs: `docker-compose logs`
3. Verify API keys in `config.py`
4. Ensure all dependencies are installed

---

**⭐ If you found this project helpful, please give it a star!**

---

*Last Updated: November 2024 | Version 1.0.0*
