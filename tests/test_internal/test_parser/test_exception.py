import pytest
from migrator.internal.parser.exception import ValidationError

TEST_MSG = "msg"


def raise_incorrect_structure_exception():
    raise ValidationError(TEST_MSG)


def test_success_raise_incorrect_structure_exception() -> None:
    with pytest.raises(ValidationError, match=TEST_MSG):
        raise_incorrect_structure_exception()
