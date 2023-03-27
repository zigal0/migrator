import pytest
import sqlite3
from migrator.internal.repository.sqlite_meta_migration import SQLiteMetaRepository


TEST_TABLE_DROP = "DROP TABLE IF EXISTS meta_migration;"


@pytest.fixture
def create_repository() -> SQLiteMetaRepository:
    con = sqlite3.connect(':memory:')
    with con:
        cur = con.cursor()
        cur.execute(TEST_TABLE_DROP)

    return SQLiteMetaRepository(con)


def test_main_flow(create_repository) -> None:
    repository = create_repository

    repository.create_version_table()

    repository.insert_version(1)
    repository.insert_version(2)
    repository.insert_version(3)

    repository.delete_version(2)

    version_ids = repository.get_ordered_migration_ids()

    assert version_ids == [1, 3]
