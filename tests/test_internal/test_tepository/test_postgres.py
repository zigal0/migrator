# import psycopg.errors
# import pytest
# from migrator.internal.repository.postgres import PostgresRepository
#
#
# def test_success_main_flow(postgresql) -> None:
#     repository = PostgresRepository(postgresql)
#
#     repository.create_version_table()
#
#     repository.insert_version(1)
#     repository.insert_version(2)
#     repository.insert_version(3)
#
#     repository.delete_version(2)
#
#     version_ids = repository.get_ordered_migration_ids()
#
#     assert version_ids == [1, 3]
