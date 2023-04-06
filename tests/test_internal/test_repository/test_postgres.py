import psycopg2
import testing.postgresql
from migrator.internal.repository.postgres import PostgresRepository
from tests.test_internal.test_repository import common


def test_success_main_flow() -> None:
    with testing.postgresql.Postgresql() as postgresql:
        con = psycopg2.connect(**postgresql.dsn())
        repository = PostgresRepository(con)

        repository.create_version_table()

        repository.apply_migration(
            version_id=1,
            queries=common.SQL_QUERIES_UP,
            mode=True,
        )

        version_ids = repository.get_ordered_migration_ids()

        assert version_ids == [1]

        repository.apply_migration(
            version_id=1,
            queries=common.SQL_QUERIES_DOWN,
            mode=False,
        )

        version_ids = repository.get_ordered_migration_ids()

        assert version_ids == []
