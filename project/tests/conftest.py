"""
pytest automatically discovers files that start or end with 'test'.
Test functions must begin with 'test_' classes must begin with 'Test'.

Starlette's TestClient uses Requests library to make requests against FastAPI app
Override dependencies (?): main.app.dependency_overrides[get_settings] = get_settings_override

fixtures start: https://pybit.es/pytest-fixtures.html
fixtures: https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session
pytest, get started: https://docs.pytest.org/en/latest/getting-started.html

Try using the 'given, when, then' framework for writing test: https://martinfowler.com/bliki/GivenWhenThen.html

Running the test: docker-compose exec web python -m pytest

yield works as finalizer / teardown of your test
"""
# project/tests/conftest.py


import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(
        testing=1, database_url=os.environ.get("DATABASE_TEST_URL")
        )


@pytest.fixture(scope="module")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down


# new
@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down
