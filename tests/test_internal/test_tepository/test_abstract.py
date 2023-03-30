import pytest
from migrator.internal.repository.sqlite import AbstractRepository


def test_fail_create_abstract_meta_repository() -> None:
    with pytest.raises(TypeError):
        AbstractRepository()


def test_success_create_subclass_meta_repository() -> None:
    class Test(AbstractRepository):
        def create_version_table(self) -> None: pass

        def apply_migration(
                self,
                version_id: int,
                queries: list[str],
                mode: bool,
        ) -> None: pass

        def get_ordered_migration_ids(self) -> list[int]: return []

    t = Test()
    assert isinstance(t, AbstractRepository)
