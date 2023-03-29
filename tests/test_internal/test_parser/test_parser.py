import pytest
from migrator.internal.parser.parser import Parser
import migrator.internal.parser.exception as exception

UP_QUERY_1 = "SELECT * FROM smth;"
UP_QUERY_2 = "SELECT * FROM smth2;"
DOWN_QUERY = "SELECT * FROM smth;"

VALID_CONTENT = f"""-- migrator up
{UP_QUERY_1} -- comment
{UP_QUERY_2}

-- migrator down
{DOWN_QUERY}
"""

INVALID_CONTENT_BY_UP = f"""-- migrator ups"""

INVALID_CONTENT_BY_DOWN = f"""-- migrator up
"""

INVALID_CONTENT_BY_STRUCTURE = f"""-- migrator down
{UP_QUERY_1}

-- migrator up
{DOWN_QUERY}
"""


def test_success_up() -> None:
    parser = Parser()

    res = parser.get_migrations_up(VALID_CONTENT)

    assert res == [UP_QUERY_1, UP_QUERY_2]


def test_success_down() -> None:
    parser = Parser()

    res = parser.get_migrations_down(VALID_CONTENT)

    assert res == [DOWN_QUERY]


def test_fail_validation_by_up() -> None:
    parser = Parser()

    with pytest.raises(
            exception.ValidationError,
            match=exception.INCORRECT_BLOCKS % ('up', 0)
    ):
        parser.get_migrations_up(INVALID_CONTENT_BY_UP)


def test_fail_validation_by_down() -> None:
    parser = Parser()

    with pytest.raises(
            exception.ValidationError,
            match=exception.INCORRECT_BLOCKS % ('down', 0)
    ):
        parser.get_migrations_down(INVALID_CONTENT_BY_DOWN)


def test_fail_validation_by_structure() -> None:
    parser = Parser()

    with pytest.raises(
            exception.ValidationError,
            match=exception.INCORRECT_STRUCTURE
    ):
        parser.get_migrations_up(INVALID_CONTENT_BY_STRUCTURE)

