import psycopg.errors
import pytest
from migrator.internal.repository.postgres_meta_migration import PostgresMetaRepository


def test_success_main_flow(postgresql) -> None:
    repository = PostgresMetaRepository(postgresql)

    repository.create_version_table()

    repository.insert_version(1)
    repository.insert_version(2)
    repository.insert_version(3)

    repository.delete_version(2)

    version_ids = repository.get_ordered_migration_ids()

    assert version_ids == [1, 3]


def test_fail_create_2nd_table(postgresql) -> None:
    repository = PostgresMetaRepository(postgresql)

    repository.create_version_table()
    with pytest.raises(psycopg.errors.DuplicateTable):
        repository.create_version_table()
