import pytest
import sqlite3
from migrator.internal.repository.sqlite import SQLiteRepository

SQL_QUERIES_UP = [
    'CREATE TABLE test (id INTEGER);',
    'INSERT INTO test (id) VALUES (2);'
]

SQL_QUERIES_DOWN = [
    'DROP TABLE test;',
]

@pytest.fixture
def create_repository() -> SQLiteRepository:
    con = sqlite3.connect(':memory:')

    return SQLiteRepository(con)


def test_success_main_flow(create_repository) -> None:
    repository = create_repository

    repository.create_version_table()

    repository.apply_migration(
        version_id=1,
        queries=SQL_QUERIES_UP,
        mode=True,
    )

    version_ids = repository.get_ordered_migration_ids()

    assert version_ids == [1]

    repository.apply_migration(
        version_id=1,
        queries=SQL_QUERIES_DOWN,
        mode=False,
    )

    version_ids = repository.get_ordered_migration_ids()

    assert version_ids == []
