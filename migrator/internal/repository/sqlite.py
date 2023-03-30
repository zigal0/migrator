"""
Module contains repository for interaction with SQLite.
"""

import sqlite3
from migrator.internal.repository.abstract import AbstractRepository
from migrator.internal.repository import sql


class SQLiteRepository(AbstractRepository):
    """ Repository for interaction with SQLite. """

    def __init__(self, con: sqlite3.Connection) -> None:
        self.con = con

    def create_version_table(self) -> None:
        with self.con:
            cur = self.con.cursor()
            _ = cur.execute(sql.CREATE_META_SQLITE)

    def get_ordered_migration_ids(self) -> list[int]:
        with self.con:
            cur = self.con.cursor()
            cur.execute(sql.GET_ORDERED_MIGRATION_IDS)
            rows = cur.fetchall()

        ids = []
        for row in rows:
            ids.append(row[0])

        return ids

    def apply_migration(
            self,
            version_id: int,
            queries: list[str],
            mode: bool,
    ) -> None:
        with self.con:
            cur = self.con.cursor()
            for query in queries:
                cur.execute(query)

            if mode:
                cur.execute(sql.INSERT_META_MIGRATION_TABLE, (version_id,))
            else:
                cur.execute(sql.DELETE_META_MIGRATION_TABLE, (version_id,))
