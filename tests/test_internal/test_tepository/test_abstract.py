import pytest
from migrator.internal.repository.sqlite_meta_migration import AbstractMetaRepository


def test_fail_create_abstract_meta_repository() -> None:
    with pytest.raises(TypeError):
        AbstractMetaRepository()


def test_success_create_subclass_meta_repository() -> None:
    class Test(AbstractMetaRepository):
        def create_version_table(self) -> None: pass
        def insert_version(self, version_id: int) -> None: pass
        def delete_version(self, version_id: int) -> None: pass
        def get_ordered_migration_ids(self) -> list[int]: return []

    t = Test()
    assert isinstance(t, AbstractMetaRepository)
