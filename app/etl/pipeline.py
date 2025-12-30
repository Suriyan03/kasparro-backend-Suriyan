import pandas as pd
import requests
import datetime
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.models import CryptoPrice
from app.core.normalization import get_canonical_symbol

# --- Source 1: CoinPaprika ---
def fetch_coinpaprika_data():
    url = "https://api.coinpaprika.com/v1/tickers"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        top_coins = [coin for coin in data if coin['rank'] <= 10]
        
        processed_data = []
        for coin in top_coins:
            processed_data.append({
                "symbol": coin['symbol'],
                "price_usd": float(coin['quotes']['USD']['price']),
                "source": "coinpaprika",
                "timestamp": datetime.datetime.now()
            })
        print(f"CoinPaprika: Fetched {len(processed_data)} records.")
        return processed_data
    except Exception as e:
        print(f"Error fetching CoinPaprika: {e}")
        return []

# --- Source 2: CoinGecko ---
def fetch_coingecko_data():
    # CoinGecko uses IDs (bitcoin, ethereum) instead of symbols
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        processed_data = []
        for coin in data:
            processed_data.append({
                "symbol": coin['symbol'].upper(), # CoinGecko uses lowercase 'btc'
                "price_usd": float(coin['current_price']),
                "source": "coingecko",
                "timestamp": datetime.datetime.now()
            })
        print(f"CoinGecko: Fetched {len(processed_data)} records.")
        return processed_data
    except Exception as e:
        print(f"Error fetching CoinGecko: {e}")
        return []

# --- Source 3: CSV ---
def fetch_csv_data():
    try:
        df = pd.read_csv("data/crypto_history.csv")
        processed_data = []
        for index, row in df.iterrows():
            processed_data.append({
                "symbol": row['symbol'],
                "price_usd": float(row['price']),
                "source": "csv",
                "timestamp": datetime.datetime.now() 
            })
        print(f"CSV: Fetched {len(processed_data)} records.")
        return processed_data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

# --- MAIN ETL FUNCTION ---
def load_data_to_db():
    db = SessionLocal()
    print("--- Starting ETL Job ---")
    
    try:
        # 1. Fetch from all 3 sources
        s1 = fetch_coinpaprika_data()
        s2 = fetch_coingecko_data()
        s3 = fetch_csv_data()
        
        # 2. Merge them
        all_data = s1 + s2 + s3
        print(f"Total records to process: {len(all_data)}")
        
        # 3. Normalize and Save
        for data in all_data:
            # Step A: Get Raw ID
            raw_symbol = data.get("symbol")
            
            # Step B: Normalize (Get the Canonical Symbol)
            canonical = get_canonical_symbol(raw_symbol)
            
            print(f"Saving: {raw_symbol} -> {canonical}")

            # Step C: Create Record with NEW Field
            db_record = CryptoPrice(
                symbol=raw_symbol,              # Old ID
                canonical_symbol=canonical,     # <--- THE FIX
                price_usd=data['price_usd'],
                source=data['source'],
                timestamp=data['timestamp']
            )
            db.add(db_record)
        
        db.commit()
        print("--- Data Saved Successfully with Normalization ---")
        
    except Exception as e:
        db.rollback()
        print(f"ETL Failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    load_data_to_db()