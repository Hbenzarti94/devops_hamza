# tests/test_app.py

import sys
import os

# Insérer le chemin relatif vers backend dans sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

# Importer l'application Flask depuis app.py dans backend
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    data = response.json
    assert 'users' in data
    assert len(data['users']) == 3  # Vérifie que trois utilisateurs sont retournés
