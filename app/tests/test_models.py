# app/tests/test_models.py

import pytest
from pydantic import ValidationError
from app.models import Usuario

def test_usuario_valid_data():
    usuario = Usuario(id=1, nombre="John Doe", email="john@example.com")
    assert usuario.nombre == "John Doe"
    assert usuario.email == "john@example.com"

def test_usuario_invalid_email():
    # Se espera que falle al no tener "@" en el email
    with pytest.raises(ValidationError):
        Usuario(id=2, nombre="Jane Doe", email="jane.example.com")

def test_usuario_nombre_demasiado_corto():
    # Se espera que falle al tener un nombre demasiado corto
    with pytest.raises(ValidationError):
        Usuario(id=3, nombre="Jo", email="jo@example.com")
