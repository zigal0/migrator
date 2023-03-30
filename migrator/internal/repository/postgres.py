# pylint: disable=duplicate-code
"""
Module contains repository for interaction with SQLite.
"""

from psycopg2.extensions import connection
from migrator.internal.repository.abstract import AbstractRepository

# SQLs
CREATE_META_MIGRATION_TABLE = """
CREATE TABLE IF NOT EXISTS meta_migration (
    version_id BIGINT,
    applied_at TIMESTAMP NOT NULL DEFAULT NOW(),
    PRIMARY KEY(version_id)
);
"""

INSERT_META_MIGRATION_TABLE = """
INSERT INTO meta_migration (version_id)
    VALUES (%s);
"""

DELETE_META_MIGRATION_TABLE = """
DELETE
FROM meta_migration
WHERE version_id = %s;
"""

GET_ORDERED_MIGRATION_IDS = """
SELECT version_id
FROM meta_migration
ORDER BY applied_at;
"""


class PostgresRepository(AbstractRepository):
    """ Repository for interaction with Postgres. """

    def __init__(self, con: connection) -> None:
        self.con = con

    def create_version_table(self) -> None:
        with self.con:
            cur = self.con.cursor()
            cur.execute(CREATE_META_MIGRATION_TABLE)

    def get_ordered_migration_ids(self) -> list[int]:
        with self.con:
            cur = self.con.cursor()
            cur.execute(GET_ORDERED_MIGRATION_IDS)
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
                cur.execute(INSERT_META_MIGRATION_TABLE, (version_id,))
            else:
                cur.execute(DELETE_META_MIGRATION_TABLE, (version_id,))
