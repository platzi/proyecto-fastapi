# app/tests/test_items.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "description": "Test description"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data

def test_read_item():
    # Se crea primero un item
    create_response = client.post("/items/", json={"name": "Read Item", "description": "Item para leer"})
    item_id = create_response.json()["id"]
    # Se consulta el item creado
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Read Item"

def test_update_item():
    # Se crea un item para actualizar
    response = client.post("/items/", json={"name": "Update Item", "description": "Antes de actualizar"})
    item = response.json()
    item_id = item["id"]
    # Se actualiza el item
    update_data = {"id": item_id, "name": "Updated Item", "description": "Después de actualizar"}
    response_put = client.put(f"/items/{item_id}", json=update_data)
    assert response_put.status_code == 200
    updated_item = response_put.json()
    assert updated_item["name"] == "Updated Item"
    assert updated_item["description"] == "Después de actualizar"

def test_delete_item():
    # Se crea un item para borrar
    create_response = client.post("/items/", json={"name": "Delete Item", "description": "Item para borrar"})
    item_id = create_response.json()["id"]
    # Se elimina el item
    response_delete = client.delete(f"/items/{item_id}")
    assert response_delete.status_code == 200
    # Se intenta obtener el item eliminado
    response_get = client.get(f"/items/{item_id}")
    assert response_get.status_code == 404

def test_list_items_pagination():
    # Se crean varios items para probar la paginación
    for i in range(1, 6):
        client.post("/items/", json={"name": f"Paginated Item {i}", "description": "Testing pagination"})
    response = client.get("/items/?limit=3&offset=1")
    assert response.status_code == 200
    items = response.json()
    # Se esperan 3 items según la paginación
    assert len(items) == 3

def test_search_items():
    # Se crean items con nombres específicos para el filtro
    client.post("/items/", json={"name": "Alpha", "description": "Primer item"})
    client.post("/items/", json={"name": "Beta", "description": "Segundo item"})
    client.post("/items/", json={"name": "Gamma", "description": "Tercer item"})

    response = client.get("/items/search?name=a&sort=asc&limit=10&offset=0")
    assert response.status_code == 200
    items = response.json()
    # Se verifica que cada item devuelto contenga la letra "a" (minúscula) en su nombre.
    for item in items:
        assert "a" in item["name"].lower()
