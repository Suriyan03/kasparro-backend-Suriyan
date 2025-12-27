from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from app.core.database import Base

class CryptoPrice(Base):
    __tablename__ = "crypto_prices"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)  # e.g., BTC
    price_usd = Column(Float)            # e.g., 50000.00
    source = Column(String)              # e.g., 'coinpaprika' or 'csv'
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Metadata for debugging
    raw_data = Column(String, nullable=True)