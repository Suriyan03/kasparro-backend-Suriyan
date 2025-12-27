import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Kasparro Backend"
    
    # OLD BROKEN LINE: ... @127.0.0.1 ...
    
    # NEW FIXED LINE: Uses 'DB_HOST' from .env (which Docker sets to 'db')
    DATABASE_URL: str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    COINPAPRIKA_API_KEY: str = os.getenv("COINPAPRIKA_API_KEY")

settings = Settings()