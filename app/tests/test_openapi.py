# app/tests/test_openapi.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_openapi_metadata():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    # Se verifica que la documentación contenga los metadatos personalizados
    assert data["info"]["title"] == "Curso de FastAPI"
    assert data["info"]["version"] == "1.0.0"
