"""
Module contains repository for interaction with SQLite meta table.
"""

from psycopg2.extensions import connection
from migrator.internal.repository.abstract import AbstractMetaRepository

# SQLs
CREATE_META_MIGRATION_TABLE = """CREATE TABLE meta_migration (
    version_id BIGINT,
    applied_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(version_id)
)"""

INSERT_META_MIGRATION_TABLE = """
INSERT INTO meta_migration (version_id) VALUES (%s)
"""

DELETE_META_MIGRATION_TABLE = """
DELETE FROM meta_migration WHERE version_id = %s
"""

GET_ORDERED_MIGRATION_IDS = """
SELECT version_id FROM meta_migration ORDER BY applied_at
"""


class PostgresMetaRepository(AbstractMetaRepository):
    """ Repository for interaction with Postgres meta table. """

    def __init__(self, con: connection) -> None:
        self.con = con

    def create_version_table(self) -> None:
        with self.con.cursor() as cur:
            cur.execute(CREATE_META_MIGRATION_TABLE)

    def insert_version(self, version_id: int) -> None:
        with self.con.cursor() as cur:
            cur.execute(INSERT_META_MIGRATION_TABLE, (version_id,))

    def delete_version(self, version_id: int) -> None:
        with self.con.cursor() as cur:
            cur.execute(DELETE_META_MIGRATION_TABLE, (version_id,))

    def get_ordered_migration_ids(self) -> list[int]:
        with self.con.cursor() as cur:
            cur.execute(GET_ORDERED_MIGRATION_IDS)

            rows = cur.fetchall()

        res = []
        for row in rows:
            res.append(row[0])

        return res
