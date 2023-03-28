"""
Main Script (need to add functional).
"""

import sys
from datetime import datetime

FILE_CONTENT = """-- +goose Up
-- SQL in this section is executed when the migration is applied.

-- +goose Down
-- SQL in this section is executed when the migration is rolled back.
"""


class Colors:  # pylint: disable=too-few-public-methods
    """ Class with set colors for logs print. """
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    DEFAULT = '\033[0m'


def print_fail_msg(msg: str) -> None:
    """ Print FAIL msg. """
    print(f"{Colors.FAIL}FAIL: " + msg + f"{Colors.DEFAULT}")


def print_warning_msg(msg: str) -> None:
    """ Print WARNING msg. """
    print(f"{Colors.WARNING}WARNING: " + msg + f"{Colors.DEFAULT}")


def print_info_msg(msg: str) -> None:
    """ Print INFO msg. """
    print(f"{Colors.INFO}INFO: " + msg + f"{Colors.DEFAULT}")


def print_success_msg(msg: str) -> None:
    """ Print SUCCESS msg. """
    print(f"{Colors.SUCCESS}SUCCESS: " + msg + f"{Colors.DEFAULT}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_fail_msg('Need to enter command.')

        sys.exit()

    CMD = sys.argv[1]

    if CMD == 'create':
        if len(sys.argv) < 3:
            print_fail_msg('Need to enter migration name.')

            sys.exit()

        migration_name = sys.argv[2]
        version_id = datetime.today().strftime("%d%m%Y%H%M%S")
        migration_file_name = version_id + '_' + migration_name + '.sql'

        with open(file=migration_file_name, mode='w', encoding="utf-8") as f:
            f.write(FILE_CONTENT)

    else:
        print_fail_msg(f'Command {CMD} is not defined.')
