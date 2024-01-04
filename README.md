## Prerequisites
- Python 3.10 or greater versions
- MySql

## Recommended tools
- PyCharm : Text Editor for Python 
- Visual studio
- phpmyadmin, Adminer : For Sql

## For making virtualenv
- Run command: python -m venv venv

#### Create .env file and set the environment variable (You can take a example from the .env.example file)

## For running migration
- alembic revision --autogenerate -m "Auto migrations"
- alembic upgrade head

## For running python server
- python run.py

#### Open up your browser and visit http://127.0.0.1:8002/docs to see all the APIs.

## Project Structure
```
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── config
│   ├── config.py
│   ├── __init__.py
│   └── logger.py
├── __init__.py
├── README.md
├── remove_alembic.py
├── requirements.txt
├── run.py
└── src
    ├── api
    │   └── v1
    │       ├── auth
    │       │   ├── crud.py
    │       │   ├── endpoints.py
    │       │   └── models.py
    │       ├── __init__.py
    │       └── staff
    │           ├── crud.py
    │           ├── endpoints.py
    │           ├── __init__.py
    │           └── schema.py
    ├── app.py
    ├── db
    │   ├── base.py
    │   ├── __init__.py
    │   └── session.py
    ├── general
    │   ├── auth_utils.py
    │   ├── constant.py
    │   ├── hash_utils.py
    │   ├── helper.py
    │   ├── __init__.py
    │   ├── response.py
    │   ├── token_utils.py
    │   └── validation_message.json
    ├── __init__.py
    └── routes
        ├── route.py
        └── v1.py
```