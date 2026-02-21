# Task Manager API

API REST desarrollada con FastAPI para gestionar tareas. Permite crear, listar, actualizar y eliminar tareas utilizando una arquitectura organizada por capas.

Proyecto enfocado en aplicar principios básicos de arquitectura backend y separación de responsabilidades.

## Tecnologías
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Estructura del proyecto

app/
- main.py: Endpoints y configuración principal
- models.py: Modelos ORM
- schemas.py: Validación de datos
- crud.py: Lógica de acceso a datos
- database.py: Configuración de la base de datos

## Instalación

1. Clonar el repositorio:
git clone https://github.com/mariomirandadev/task-manager-api.git

2. Crear entorno virtual:
python -m venv venv

3. Instalar dependencias:
pip install -r requirements.txt

## Ejecutar

uvicorn app.main:app --reload

Después abrir:
http://127.0.0.1:8000/docs

## Funcionalidades
- Crear tarea
- Listar tareas
- Actualizar tarea
- Eliminar tarea

## Mejoras futuras
- Autenticación de usuarios
- Despliegue en la nube
- Pruebas unitarias