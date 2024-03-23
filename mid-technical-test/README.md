# Python Backend Developer MID

Este es un proyecto que utiliza FastAPI como framework web y PostgreSQL como base de datos, todo en contenedores Docker.
Proporciona una estructura básica para comenzar a desarrollar una aplicación web con Python.

## Requisitos previos
- Docker: Instalación de Docker
- Docker Compose: Instalación de Docker Compose


## Instrucciones de instalación

Crea un archivo `.env` en el directorio raíz del proyecto y configura las variables de entorno necesarias.
Puedes copiar el archivo .env.example y modificarlo según tus necesidades:

```bash
cp .env.example .env
```

Tienes un comandos de Makefile que te pueden ser de ayuda:

```
Usage: make <target>

app          Run app with docker
clean        Remove all temporary files like pycache
help         show the help
install      Install and setup project dependencies
lint         Run linters
start        Init development server
test         Run all the tests with docker
update_libs  update libs + generate new lockfile & requirements
virtualenv   Create a virtual environment.
```

es decir, que si quieres levantar el proyecto con docker, solo debes ejecutar el comando

```bash
make app
```

Esto iniciará los contenedores de FastAPI y PostgreSQL en segundo plano.


### Accede a FastAPI en tu navegador:
- FastAPI: http://localhost:8000
- Documentación Swagger de FastAPI: http://localhost:8000/docs
- Documentación ReDoc de FastAPI: http://localhost:8000/redoc

## Estructura del proyecto

```
.
├── Makefile
├── README.md
├── docker-compose.yml
├── envs.sh
├── poetry.lock
├── pyproject.toml
└── src
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── healthcheck
    │   │   ├── __init__.py
    │   │   ├── endpoints.py
    │   │   ├── schemas.py
    │   │   └── tests
    │   │       ├── __init__.py
    │   │       └── test_endpoints.py
    │   ├── routers.py
    │   └── v1
    │       ├── __init__.py
    │       ├── costumers
    │       │   ├── __init__.py
    │       │   ├── endpoints.py
    │       │   └── tests
    │       │       └── __init__.py
    │       └── loans
    │           ├── __init__.py
    │           ├── endpoints.py
    │           └── tests
    │               └── __init__.py
    ├── core
    │   ├── __init__.py
    │   ├── middlewares
    │   │   ├── __init__.py
    │   │   ├── catcher.py
    │   │   └── trailing_slash.py
    │   ├── settings
    │   │   ├── __init__.py
    │   │   └── base.py
    │   └── utils
    │       ├── __init__.py
    │       ├── datetime.py
    │       ├── exceptions.py
    │       ├── responses.py
    │       └── validations.py
    ├── db
    │   ├── __init__.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── models.py
    │   ├── session.py
    │   └── utils.py
    ├── main.py
    └── tests
        ├── __init__.py
        └── unit
```

`19 directories, 42 files`


- `src/`: Es el directorio principal que contiene todo el código de la aplicación.
- `api/`: Contiene los módulos relacionados con la API de la aplicación.
- `core/`: Contiene los módulos centrales de la aplicación, como configuraciones y utilidades.
- `db/`: Contiene los módulos relacionados con la base de datos, incluyendo la definición de modelos y configuración de sesiones.
- `tests/`: Es el directorio para las pruebas de la aplicación.
- `Makefile`: Archivo para definir comandos y tareas comunes.
- `README.md`: Documentación del proyecto.
- `docker-compose.yml`: Archivo de configuración para ejecutar la aplicación con Docker Compose.
- `poetry.lock y pyproject.toml`: Archivos generados por Poetry para manejar las dependencias del proyecto.
Overview
The codebase is a RESTful API built with FastAPI. It provides endpoints for managing customers and loans.

# Endpoints
# Customers
```
/customers/List: Retrieves a list of all customers.
/customers/Update: Updates a customer's information.
/customers/Delete: Deletes a customer.
/customers/Create: Creates a new customer.
/customers/Retrieve: Retrieves a specific customer.
```
These endpoints allow you to interact with the customer data stored in the database.

# Loans
```
/loans/List: Retrieves a list of all loans.
/loans/Update: Updates a loan's information.
/loans/Delete: Deletes a loan.
/loans/Create: Creates a new loan.
/loans/Retrieve: Retrieves a specific loan.
```
These endpoints allow you to interact with the loan data stored in the database.

# Database
The API uses a SQLite database for storing customer and loan data. The database models are defined in db/models.py.

# Testing
Unit tests are included in the src/api/v1/costumers/tests/ and src/api/v1/loans/tests/ directories. You can run the tests using pytest.

# Installation
Clone the repository.
Ah, got it! Here's the updated installation section that includes using the Makefile:
Run make app to build the Docker image and start the API container.
The API will be available at http://0.0.0.0:9000.
Make sure you have Docker and Docker Compose installed on your machine to run the Makefile targets.

