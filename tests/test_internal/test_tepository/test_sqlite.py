# import pytest
# import sqlite3
# from migrator.internal.repository.sqlite import SQLiteRepository
#
#
# @pytest.fixture
# def create_repository() -> SQLiteRepository:
#     con = sqlite3.connect(':memory:')
#
#     return SQLiteRepository(con)
#
#
# def test_success_main_flow(create_repository) -> None:
#     repository = create_repository
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
#
#
# def test_fail_create_2nd_table(create_repository) -> None:
#     repository = create_repository
#
#     repository.create_version_table()
#     with pytest.raises(sqlite3.OperationalError):
#         repository.create_version_table()
