# app/tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_secure_endpoint_no_auth():
    response = client.get("/secure/")
    # Sin credenciales se espera 401 Unauthorized
    assert response.status_code == 401

def test_secure_endpoint_invalid_auth():
    response = client.get("/secure/", auth=("usuario", "contraseña_incorrecta"))
    assert response.status_code == 401

def test_secure_endpoint_valid_auth():
    # Se utiliza la combinación correcta (usuario: admin, contraseña: secret)
    response = client.get("/secure/", auth=("admin", "secret"))
    assert response.status_code == 200
    data = response.json()
    assert "Bienvenido" in data["message"]
