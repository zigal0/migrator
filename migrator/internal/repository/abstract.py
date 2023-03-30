"""
Module contains abstract repositories for database.
"""

from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Abstract repository for migration meta info tables and executing queries.
    """

    @abstractmethod
    def create_version_table(self) -> None:
        """ Creates new meta table. """

    @abstractmethod
    def get_ordered_migration_ids(self) -> list[int]:
        """
        Returns migration ids ordered by applied_at.
        Returns:
             List of applied migration ids.
        """

    @abstractmethod
    def apply_migration(
            self,
            version_id: int,
            queries: list[str],
            mode: bool,
    ) -> None:
        """ Executes given query. """
