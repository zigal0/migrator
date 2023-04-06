"""
Declaration and description errors that can arise during parsing.
"""

INCORRECT_BLOCKS_MSG = "Incorrect number of 'migrator %s' blocks, actual = %s."
INCORRECT_STRUCTURE_MSG = "Incorrect structure."
META_MIGRATION_MSG = "Migration contains manipulation with meta_migration " \
                     "table 'not allowed'."


class ValidationError(Exception):
    """ Raised when script structure is incorrect. """


class MetaMigrationChangeError(Exception):
    """ Raised when script contains manipulation with meta_migration table. """
