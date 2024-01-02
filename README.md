## Project Structure
```
├── alembic
│   ├── env.py
│   │   ├── env.cpython-310.pyc
│   │   └── env.cpython-38.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       
├── alembic.ini
├── config
│   ├── config.py
│   ├── __init__.py
│   ├── logger.py
│   └── __pycache__
│       ├── config.cpython-310.pyc
│       ├── config.cpython-38.pyc
│       ├── __init__.cpython-310.pyc
│       ├── __init__.cpython-38.pyc
│       ├── logger.cpython-310.pyc
│       └── logger.cpython-38.pyc
├── __init__.py
├── README.md
├── remove_alembic.py
├── requirements.txt
├── run.py
└── src
    ├── api
    │   └── v1
    │       ├── auth
    │       │   ├── models.py
    │       │   └── __pycache__
    │       │       └── models.cpython-310.pyc
    │       ├── __init__.py
    │       ├── __pycache__
    │       │   └── __init__.cpython-310.pyc
    │       └── staff
    │           ├── crud.py
    │           ├── endpoints.py
    │           ├── __init__.py
    │           ├── __pycache__
    │           │   ├── crud.cpython-310.pyc
    │           │   ├── endpoints.cpython-310.pyc
    │           │   ├── __init__.cpython-310.pyc
    │           │   └── schema.cpython-310.pyc
    │           └── schema.py
    ├── app.py
    ├── db
    │   ├── base.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── base.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   └── session.cpython-310.pyc
    │   └── session.py
    ├── general
    │   ├── constant.py
    │   ├── helper.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── helper.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   └── response.cpython-310.pyc
    │   ├── response.py
    │   └── validation_message.json
    ├── __init__.py
    ├── __pycache__
    │   ├── app.cpython-310.pyc
    │   └── __init__.cpython-310.pyc
    └── routes
        ├── __pycache__
        │   ├── route.cpython-310.pyc
        │   ├── route.cpython-38.pyc
        │   ├── v1.cpython-310.pyc
        │   └── v1.cpython-38.pyc
        ├── route.py
        └── v1.py
```