## Project Structure
```
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── d7c7b8589b42_auto_migrations.py
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
    │   ├── constant.py
    │   ├── helper.py
    │   ├── __init__.py
    │   ├── response.py
    │   └── validation_message.json
    ├── __init__.py
    └── routes
        ├── route.py
        └── v1.py
```