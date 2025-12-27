from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.schemas.models import CryptoPrice
# We import the ETL function
from app.etl.pipeline import load_data_to_db

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kasparro Backend")

# --- AUTO-RUN DATA ON STARTUP ---
@app.on_event("startup")
def startup_event():
    print("Booting up... Loading Data...")
    try:
        load_data_to_db()
        print("Data loaded successfully on startup!")
    except Exception as e:
        print(f"Error loading data: {e}")

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

@app.get("/data")
def get_crypto_data(db: Session = Depends(get_db)):
    records = db.query(CryptoPrice).all()
    return {
        "metadata": {"count": len(records)},
        "data": records
    }