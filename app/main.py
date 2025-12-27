from fastapi import FastAPI
from app.core.database import engine, Base
from app.api import routes

# Create the database tables (Automatic check on startup)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kasparro Crypto Backend")

# Include the routes we just made
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Kasparro Crypto API. Go to /docs for testing."}