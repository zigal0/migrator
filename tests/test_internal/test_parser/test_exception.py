import pytest
from migrator.internal.parser.exception import ValidationError, MetaMigrationChangeError

TEST_MSG = "msg"


def raise_validation_error():
    raise ValidationError(TEST_MSG)


def test_success_incorrect_structure_exception() -> None:
    with pytest.raises(ValidationError, match=TEST_MSG):
        raise_validation_error()


def raise_meta_migration_change_error():
    raise MetaMigrationChangeError(TEST_MSG)


def test_success_meta_migration_change_error() -> None:
    with pytest.raises(MetaMigrationChangeError, match=TEST_MSG):
        raise_meta_migration_change_error()
