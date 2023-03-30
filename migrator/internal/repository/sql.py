"""
SQL queries for databases.
"""

CREATE_META_SQLITE = """
CREATE TABLE IF NOT EXISTS meta_migration (
    version_id INTEGER,
    applied_at TIMESTAMP DEFAULT (DATETIME('now')),
    PRIMARY KEY(version_id)
);
"""

CREATE_META_POSTGRES = """
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
