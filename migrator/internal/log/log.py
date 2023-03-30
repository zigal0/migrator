"""
Represents custom logger function.
"""


class Colors:  # pylint: disable=too-few-public-methods
    """ Class with set colors for logs print. """
    INFO = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    DEFAULT = '\033[0m'


def log_fail_msg(msg: str) -> None:
    """ Print FAIL msg. """
    print(f"{Colors.FAIL}FAIL: " + msg + f"{Colors.DEFAULT}")


def log_warning_msg(msg: str) -> None:
    """ Print WARNING msg. """
    print(f"{Colors.WARNING}WARNING: " + msg + f"{Colors.DEFAULT}")


def log_info_msg(msg: str) -> None:
    """ Print INFO msg. """
    print(f"{Colors.INFO}INFO: " + msg + f"{Colors.DEFAULT}")


def log_success_msg(msg: str) -> None:
    """ Print SUCCESS msg. """
    print(f"{Colors.SUCCESS}SUCCESS: " + msg + f"{Colors.DEFAULT}")
