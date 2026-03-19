import os
import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:15") as postgres:
        os.environ["DATABASE_URL"] = postgres.get_connection_url()
        yield postgres