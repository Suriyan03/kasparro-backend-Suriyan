from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db
from app.schemas.models import CryptoPrice
import time

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """
    Checks if the database is reachable.
    """
    try:
        # Try a simple SQL query to check connection
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@router.get("/data")
def get_crypto_data(
    skip: int = 0, 
    limit: int = 10, 
    symbol: str = None,
    db: Session = Depends(get_db)
):
    """
    Fetch crypto data with pagination and filtering.
    """
    start_time = time.time()
    
    query = db.query(CryptoPrice)
    
    # Apply filter if user provided a symbol (e.g., ?symbol=BTC)
    if symbol:
        query = query.filter(CryptoPrice.symbol == symbol)
    
    # Apply pagination
    results = query.offset(skip).limit(limit).all()
    
    # Calculate how long the request took (Latency)
    process_time_ms = (time.time() - start_time) * 1000
    
    return {
        "metadata": {
            "count": len(results),
            "latency_ms": round(process_time_ms, 2)
        },
        "data": results
    }