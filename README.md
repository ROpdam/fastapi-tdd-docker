# Test-Driven Development with FastAPI and Docker

![Continuous Integration and Delivery](https://github.com/ropdam/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)

Completed this course from [testdriven](https://testdriven.io/)
```
├── .github
│   └── workflows
│       └── main.yml
├── .gitignore
├── README.md
├── docker-compose.yml
├── project
│   ├── .coverage
│   ├── .coveragerc
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── app
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── crud.py
│   │   │   ├── ping.py
│   │   │   └── summaries.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── pydantic.py
│   │   │   └── tortoise.py
│   │   └── summarizer.py
│   ├── db
│   │   ├── Dockerfile
│   │   └── create.sql
│   ├── entrypoint.sh
│   ├── htmlcov
│   ├── requirements-dev.txt
│   ├── requirements.txt
│   ├── setup.cfg
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       ├── test_ping.py
│       ├── test_summaries.py
│       └── test_summaries_unit.py
└── release.sh
```
