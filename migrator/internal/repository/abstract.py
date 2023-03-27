"""
Module contains abstract repositories for database.
"""

from abc import ABC, abstractmethod


class AbstractMetaRepository(ABC):
    """ Abstract repository for migration meta info tables. """

    @abstractmethod
    def create_version_table(self) -> None:
        """ Creates new meta table. """

    @abstractmethod
    def insert_version(self, version_id: int) -> None:
        """ Inserts new migration to table. """

    @abstractmethod
    def delete_version(self, version_id: int) -> None:
        """ Deletes migration from table. """

    @abstractmethod
    def get_ordered_migration_ids(self) -> list[int]:
        """ Returns migration ids ordered by applied_at. """
