# Curso de FastAPI - Proyecto Base

Este repositorio es la base para el "Curso de FastAPI". Aquí aprenderás a construir APIs REST eficientes utilizando FastAPI, validación de datos con Pydantic, integración con bases de datos relacionales a través de SQLModel (utilizando SQLite de ejemplo), implementación de middlewares, pruebas unitarias con Pytest, y estrategias de autenticación y seguridad.

## Características

- **Desarrollo rápido de APIs REST:** Potencia la creación de endpoints con FastAPI.
- **Validación de datos:** Usa Pydantic para validar y documentar los modelos de datos.
- **Documentación automática:** Integrada con Swagger (/docs y /redoc).
- **Integración con bases de datos:** Mediante SQLModel y SQLite (extensible a otras bases relacionales).
- **Middlewares personalizados:** Implementa logging, medición de tiempos de respuesta y manejo de errores.
- **Pruebas unitarias:** Configuradas con Pytest para asegurar el correcto funcionamiento de los endpoints.
- **Seguridad y autenticación:** Ejemplo de autenticación básica con HTTPBasicCredentials.
- **Arquitectura escalable:** Modularización que favorece el mantenimiento y escalado de la aplicación.

## Estructura del Proyecto

```plaintext
.
├── app/
│   ├── main.py           # Archivo principal que arranca la aplicación
│   ├── models.py         # Modelos de datos (Pydantic y SQLModel)
│   ├── routers/          # Endpoints organizados por recursos
│   ├── core/             # Configuración, middlewares y settings
│   ├── db/               # Conexión y configuración de la base de datos
│   └── tests/            # Pruebas unitarias con Pytest
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## Instalación y Configuración
### Requisitos
- Python 3.8+
- pip

### Instrucciones de Instalación
Clona el repositorio:

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
```

### Crea un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate     # En Linux/MacOS
venv\Scripts\activate        # En Windows
```

### Instala las dependencias:

```bash
pip install -r requirements.txt
```

### Ejecución
Para iniciar el servidor en modo desarrollo, ejecuta:

```bash
uvicorn app.main:app --reload
Accede a la documentación interactiva en http://localhost:8000/docs.
```

### Pruebas Unitarias
Para ejecutar las pruebas, utiliza:
```bash
pytest
```

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o tienes sugerencias, abre un issue o envía un pull request.
