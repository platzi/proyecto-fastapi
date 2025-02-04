# app/tests/test_middleware.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_logging_middleware(capsys):
    # Se realiza una petición para activar el middleware de logging
    client.get("/items/")
    # Se captura la salida estándar
    captured = capsys.readouterr().out
    # Se verifica que en el log aparezca el método y ruta
    assert "GET /items" in captured
