import pytest 
from app import app
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_returns_200(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_returns_cicd_message(client):
    response = client.get('/')
    assert b'Welcome to the CICD Docker Web App!' in response.data