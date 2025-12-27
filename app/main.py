from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.schemas.models import CryptoPrice
from app.etl.pipeline import load_data_to_db  # <--- 1. ADD THIS IMPORT

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kasparro Backend")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}

# --- 2. ADD THIS NEW ENDPOINT ---
@app.get("/refresh-data")
def trigger_etl():
    """Manually triggers the ETL pipeline to populate the DB."""
    try:
        load_data_to_db()
        return {"status": "success", "message": "Data saved successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
# --------------------------------

@app.get("/data")
def get_crypto_data(db: Session = Depends(get_db)):
    # ... (Keep your existing code here) ...
    # (Just verifying you don't delete the /data endpoint)
    records = db.query(CryptoPrice).all()
    return {
        "metadata": {"count": len(records)},
        "data": records
    }