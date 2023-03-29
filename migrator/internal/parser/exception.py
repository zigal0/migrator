"""
Declaration and description errors that can arise during parsing.
"""

INCORRECT_BLOCKS = "Incorrect number of 'migrator %s' blocks, actual = %s."
INCORRECT_STRUCTURE = "Incorrect structure."


class ValidationError(Exception):
    """ Raised when script structure is incorrect. """
