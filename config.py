# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "CG-QyGpP9GNrTr3JbMhccz44NNK")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "6TQGHX141G525IFWW2CQ2IUGKJ8SARWFXN")

# MongoDB Configuration
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
MONGO_USER = os.getenv("MONGO_USER", "admin")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "cryptopass123")
MONGO_DB = os.getenv("MONGO_DB", "cryptograph")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource=admin"

# Neo4j Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "cryptopass123")