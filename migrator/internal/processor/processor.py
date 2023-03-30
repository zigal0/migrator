"""
Processor contains main logic of migrator.
"""

from datetime import datetime
import os
from migrator.internal.parser.parser import Parser
from migrator.internal.repository.abstract import AbstractRepository
from migrator.internal.log.log import (
    log_fail_msg, log_info_msg, log_success_msg
)

FILE_CONTENT = """-- migrator up
-- SQL in this section is executed when the migration is applied.

-- migrator down
-- SQL in this section is executed when the migration is rolled back.
"""


def create_migration_file(path: str, name: str) -> None:
    """
    Creates new migration file.
    Args:
        path: where file would be created.
        name: name of migration file.
    """
    version_id = datetime.today().strftime("%d%m%Y%H%M%S")
    name = version_id + '_' + name + '.sql'
    migration_file_name = '/'.join([path, name])

    with open(file=migration_file_name, mode='w', encoding="utf-8") as file:
        file.write(FILE_CONTENT)

    log_success_msg(f'File {name} created')


class Processor:
    """
    Processor defines main functional of migrator.
    """

    def __init__(
            self,
            parser: Parser,
            repos: dict[str, AbstractRepository],
            migration_path: str,
    ):
        self.parser = parser
        self.repos = repos
        self.migration_path = migration_path

    def migrate_up(self) -> None:
        """ Runs all sql scripts in up mode. """
        for db_name, repo in self.repos.items():
            log_info_msg(f'Migrations for {db_name} started applying.')

            repo.create_version_table()
            applied_version_ids = repo.get_ordered_migration_ids()

            migration_files = os.listdir(
                '/'.join([self.migration_path, db_name])
            )
            migration_files = sorted(
                [migration_file for migration_file in migration_files
                    if migration_file.endswith('.sql')]
            )

            for migration_file in migration_files:
                file_name_parts = migration_file.split('_')

                try:
                    version_id = int(file_name_parts[0])
                except ValueError:
                    log_fail_msg(f'Incorrect migration name: {migration_file}')

                    continue  # zigal0TODO

                if version_id in applied_version_ids:
                    continue

                path_to_file = '/'.join(
                    [self.migration_path, db_name, migration_file]
                )
                with open(path_to_file, mode='r', encoding='utf-8') as file:
                    sql_script = file.read()

                sql_queries = self.parser.get_migrations_up(sql_script)

                repo.apply_migration(version_id, sql_queries, True)
                log_success_msg(f'Migration {migration_file} applied.')

    def migrate_down(self) -> None:
        """ Runs all sql scripts in down mode. """
        for db_name, repo in self.repos.items():
            log_info_msg(f'Migrations for {db_name} started applying.')

            repo.create_version_table()
            applied_version_ids = repo.get_ordered_migration_ids()

            if len(applied_version_ids) == 0:
                continue

            migration_files = os.listdir(
                '/'.join([self.migration_path, db_name])
            )
            migration_files = sorted(
                [migration_file for migration_file in migration_files
                    if migration_file.endswith('.sql')],
                reverse=True,
            )

            for migration_file in migration_files:
                file_name_parts = migration_file.split('_')

                try:
                    version_id = int(file_name_parts[0])
                except ValueError:
                    log_fail_msg(f'Incorrect migration name: {migration_file}')

                    continue  # zigal0TODO

                if version_id not in applied_version_ids:
                    continue

                path_to_file = '/'.join(
                    [self.migration_path, db_name, migration_file]
                )
                with open(path_to_file, mode='r', encoding='utf-8') as file:
                    sql_script = file.read()

                sql_queries = self.parser.get_migrations_down(sql_script)

                repo.apply_migration(version_id, sql_queries, False)
                log_success_msg(f'Migration {migration_file} applied.')
