# 🚀 Kasparro Backend Assignment

A production-ready **ETL Pipeline** and **REST API** designed to aggregate cryptocurrency data from multiple sources (APIs & CSVs), **normalize** disparate identities into a canonical format, and serve it via a high-performance backend.

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Multi_Stage-2496ED?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-336791?style=for-the-badge&logo=postgresql)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render)

---

## 🌐 Live Deployment
The application is deployed on the cloud and fully operational.

| Service | URL | Description |
| :--- | :--- | :--- |
| **Main API** | [**Live Link**](https://kasparro-api-dtmv.onrender.com/data) | Returns the aggregated & normalized JSON data. |
| **Docs (Swagger)** | [**Docs Link**](https://kasparro-api-dtmv.onrender.com/docs) | Interactive API documentation. |
| **Health Check** | [**Health Link**](https://kasparro-api-dtmv.onrender.com/health) | Verifies system status. |

---

## 🛠 Features & Architecture

### ✅ Phase 1: Ingestion & Infrastructure
* **Multi-Source Extraction:** Fetches live data from **CoinPaprika**, **CoinGecko**, and local **CSV** archives.
* **Dockerized Architecture:** Uses **Multi-Stage Docker Builds** for optimized, lightweight production images.
* **Robust Database:** PostgreSQL containerized with persistent storage.

### ✅ Phase 2: Normalization (Identity Unification)
The system solves the "Entity Resolution" problem where different sources name coins differently (e.g., `btc-bitcoin` vs `bitcoin`).
* **Normalization Layer:** A dedicated module maps diverse IDs to a single **`canonical_symbol`**.
* **Example:** * Source A (`btc-bitcoin`) ➝ **BTC**
    * Source B (`bitcoin`) ➝ **BTC**
* **Outcome:** Cleaner data for downstream analytics.

### ✅ Phase 3: Automation & Reliability
* **Auto-Startup ETL:** The pipeline triggers automatically upon container startup.
* **Makefile Support:** Standardized commands for build and deployment consistency.
* **Graceful Error Handling:** Retries and failure logging for external API calls.

---

## ⚙️ Tech Stack

* **Language:** Python 3.9
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **Containerization:** Docker (Multi-Stage) & Docker Compose
* **DevOps:** Makefile automation
* **Testing:** Pytest & HTTPX
* **Cloud:** Render

---

## 🏃‍♂️ Quick Start (Local)

This project uses a `Makefile` for simplified commands.

### 1. Clone the Repository
```bash
git clone https://github.com/Suriyan03/kasparro-backend-Suriyan.git
cd kasparro-backend-Suriyan
```

### 2. Configure Environment

Create a `.env` file in the root directory:

```env
DB_USER=postgres
DB_PASSWORD=admin
DB_NAME=kasparro_db
DB_HOST=db
DB_PORT=5432
```

### 3. Run with Make (Recommended)

```bash
make build   # Build the multi-stage Docker image
make up      # Start the application
```

The server will start at http://localhost:8000/data and automatically fetch/normalize data.

### 4. Other Commands

```bash
make logs    # View live server logs
make test    # Run the Pytest suite
make down    # Stop and remove containers
```

## 📂 Project Structure

```plaintext
├── app/
│   ├── core/
│   │   ├── database.py       # DB connection
│   │   └── normalization.py  # Logic to map IDs to Canonical Symbols
│   ├── etl/
│   │   ├── fetchers.py       # API & CSV extraction logic
│   │   └── pipeline.py       # Main ETL control flow
│   ├── schemas/              # Pydantic & SQLAlchemy models
│   └── main.py               # API entry point
├── data/
│   └── crypto_history.csv    # Historical data source
├── tests/                    # Pytest suite
├── docker-compose.yml        # Orchestration
├── Dockerfile                # Multi-stage image definition
├── Makefile                  # Shortcut commands
└── requirements.txt          # Dependencies
```
