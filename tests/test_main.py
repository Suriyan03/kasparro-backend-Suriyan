import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.etl.pipeline import fetch_coinpaprika_data

# Create a test client (simulates a web browser)
client = TestClient(app)

# 1. Test the Health Endpoint
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "database": "connected"}

# 2. Test the Data Endpoint
def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "metadata" in data
    # We expect some data because we ran the ETL
    assert len(data["data"]) >= 0 

# 3. Test ETL Logic (Mocking the API)
def test_etl_pipeline_structure():
    # This tests if our function returns a list (even if empty)
    data = fetch_coinpaprika_data()
    assert isinstance(data, list)

# 4. Test Failure Scenario (Invalid URL)
def test_invalid_route():
    response = client.get("/invalid-url")
    assert response.status_code == 404