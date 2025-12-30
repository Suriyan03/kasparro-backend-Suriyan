from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base
from datetime import datetime

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)           # e.g., "btc-bitcoin" (Original)
    canonical_symbol = Column(String, index=True) # e.g., "BTC" (Unified) <--- ADD THIS
    price_usd = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source = Column(String)