# Map different API IDs to a single standard Symbol
COIN_MAPPING = {
    # Bitcoin variations
    "btc-bitcoin": "BTC",      # CoinPaprika
    "bitcoin": "BTC",          # CoinGecko
    "BTC": "BTC",              # CSV/Standard

    # Ethereum variations
    "eth-ethereum": "ETH",
    "ethereum": "ETH",
    "ETH": "ETH",

    # Tether variations
    "usdt-tether": "USDT",
    "tether": "USDT",
    "USDT": "USDT",
    
    # Binance Coin
    "bnb-binance-coin": "BNB",
    "binancecoin": "BNB",
    "BNB": "BNB",

    # Solana
    "sol-solana": "SOL",
    "solana": "SOL",
    "SOL": "SOL"
}

def get_canonical_symbol(raw_symbol_or_id: str) -> str:
    """
    Converts a raw API ID (e.g., 'btc-bitcoin') into a standard Symbol (e.g., 'BTC').
    """
    if not raw_symbol_or_id:
        return "UNKNOWN"
    
    # Normalize to lowercase for matching
    key = raw_symbol_or_id.lower().strip()
    
    # Return the mapped value, or upper-case original if not found
    return COIN_MAPPING.get(key, raw_symbol_or_id.upper())