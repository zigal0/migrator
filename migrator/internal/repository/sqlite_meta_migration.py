"""
Module contains repository for interaction with SQLite meta table.
"""

import sqlite3
from migrator.internal.repository.abstract import AbstractMetaRepository

# SQLs
CREATE_META_MIGRATION_TABLE = """
CREATE TABLE meta_migration (
    version_id INTEGER,
    applied_at TIMESTAMP DEFAULT (DATETIME('now')),
    PRIMARY KEY(version_id)
);
"""

INSERT_META_MIGRATION_TABLE = """
INSERT INTO meta_migration (version_id) VALUES (?);
"""

DELETE_META_MIGRATION_TABLE = """
DELETE FROM meta_migration WHERE version_id = ?;
"""

GET_ORDERED_MIGRATION_IDS = """
SELECT version_id FROM meta_migration ORDER BY applied_at;
"""


class SQLiteMetaRepository(AbstractMetaRepository):
    """ Repository for interaction with SQLite meta table. """

    def __init__(self, con: sqlite3.Connection) -> None:
        self.con = con

    def create_version_table(self) -> None:
        with self.con:
            cur = self.con.cursor()
            _ = cur.execute(CREATE_META_MIGRATION_TABLE)

    def insert_version(self, version_id: int) -> None:
        with self.con:
            cur = self.con.cursor()
            _ = cur.execute(INSERT_META_MIGRATION_TABLE, [version_id])

    def delete_version(self, version_id: int) -> None:
        with self.con:
            cur = self.con.cursor()
            _ = cur.execute(DELETE_META_MIGRATION_TABLE, [version_id])

    def get_ordered_migration_ids(self) -> list[int]:
        with self.con:
            cur = self.con.cursor()
            rows = cur.execute(GET_ORDERED_MIGRATION_IDS)

        res = []
        for row in rows.fetchall():
            res.append(row[0])

        return res
