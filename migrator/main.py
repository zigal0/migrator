"""
Main script which runs migrator.
"""

import sys
import os
import sqlite3
import psycopg2
import local_config as cfg
from migrator.internal.parser.parser import Parser
from migrator.internal.processor.processor import (
    Processor, create_migration_file
)
from migrator.internal.repository.abstract import AbstractRepository
from migrator.internal.repository.postgres import PostgresRepository
from migrator.internal.repository.sqlite import SQLiteRepository
from migrator.internal.log.log import (
    log_fail_msg, log_info_msg
)


def connect_create_repositories() -> dict[str, AbstractRepository]:
    """
    Connect to databases listed in cfg.MIGRATION_DIR
    and creates repository for interaction with them.
    Returns:
        dict: key - name of database, value - repository
    """
    db_names = os.listdir(cfg.MIGRATION_PATH)
    repos = {}
    for db_name in db_names:
        if db_name == 'postgres':
            postgres_con = psycopg2.connect(
                database=cfg.POSTGRES_DB,
                host=cfg.HOST,
                user=cfg.POSTGRES_USER,
                password=cfg.POSTGRES_PASSWORD,
                port=cfg.POSTGRES_PORT,
            )
            postgres_repo: AbstractRepository = PostgresRepository(postgres_con)

            repos['postgres'] = postgres_repo

        elif db_name == 'sqlite':
            sqlite_con = sqlite3.connect(cfg.SQLITE_DB_FILE)

            sqlite_repo: AbstractRepository = SQLiteRepository(sqlite_con)

            repos['sqlite'] = sqlite_repo

    return repos


if __name__ == '__main__':
    if len(sys.argv) < 2:
        log_fail_msg('Need to enter command.')

        sys.exit()

    CMD = sys.argv[1]

    if CMD == 'create':
        if len(sys.argv) < 4:
            log_fail_msg('Need to enter database name and migration name.')

            sys.exit()

        create_migration_file(sys.argv[2], sys.argv[3])

    if CMD == 'migrate':
        if len(sys.argv) < 3 and sys.argv[2] not in ['up', 'down']:
            log_fail_msg('Need to enter one of modes [up, down].')

            sys.exit()

        migrator = Processor(
            Parser(),
            connect_create_repositories(),
            cfg.MIGRATION_PATH,
        )

        if sys.argv[2] == 'up':
            migrator.migrate_up()
        else:
            migrator.migrate_down()

    elif CMD == 'help':
        log_info_msg("Need help.")

    else:
        log_fail_msg(f'Command {CMD} is not defined.')
