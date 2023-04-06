"""
Module contains parser that parse sql migration files.
"""

import re
import migrator.internal.parser.exception as exceptions

# Regular expressions for parsing
RE_ALL = r"([\S\s]*)"
RE_NEW_LINE = r"(?:\r\n|\r|\n)"
RE_UP = r"-- migrator up" + RE_NEW_LINE
RE_DOWN = r"-- migrator down" + RE_NEW_LINE
RE_COMMENT = r"--.*" + RE_NEW_LINE
REGEX = RE_UP + RE_ALL + RE_DOWN + RE_ALL


class Parser:
    """
    Parser parse sql script.
    """

    def __init__(self) -> None:
        self._template_re = re.compile(REGEX)
        self._re_up = re.compile(RE_UP)
        self._re_down = re.compile(RE_DOWN)
        self._re_comment = re.compile(RE_COMMENT)

    def get_migrations_up(self, script: str) -> list[str]:
        """
        Returns up sql queries.
        Args:
            script: sql script.
        Returns:
            list of up sql queries.
        Raises:
            ValidationError: if structure of sql script is incorrect.
        """
        return self._parse_by_mode(script, True)

    def get_migrations_down(self, script: str) -> list[str]:
        """
        Returns down sql queries.
        Args:
            script: sql script.
        Returns:
            list of down sql queries.
        Raises:
            ValidationError: if structure of sql script is incorrect.
        """
        return self._parse_by_mode(script, False)

    def _parse_by_mode(self, script: str, mode: bool) -> list[str]:
        """
        Returns sql queries by given mode.
        Args:
            script: file with sql scripts.
            mode: migration mode (True - up, False - Down).
        Returns:
            list of sql queries.
        Raises:
            ValidationError: if structure of sql script is incorrect.
        """
        if 'meta_migration' in script:
            raise exceptions.MetaMigrationChangeError(
                exceptions.META_MIGRATION_MSG
            )

        if len(self._re_up.findall(script)) != 1:
            up_blocks_number = len(self._re_up.findall(script))
            raise exceptions.ValidationError(
                exceptions.INCORRECT_BLOCKS_MSG % ('up', up_blocks_number)
            )

        if len(self._re_down.findall(script)) != 1:
            down_blocks_number = len(self._re_down.findall(script))
            raise exceptions.ValidationError(
                exceptions.INCORRECT_BLOCKS_MSG % ('down', down_blocks_number)
            )

        match_res = self._template_re.match(script)
        if match_res is None:
            raise exceptions.ValidationError(
                exceptions.INCORRECT_STRUCTURE_MSG
            )

        parts = match_res.groups()
        if mode:
            to_parse = parts[0]
        else:
            to_parse = parts[1]

        to_parse = self._re_comment.sub('', to_parse)
        queries = to_parse.split(';')
        queries = [query.strip() for query in queries]
        queries = list(filter(None, queries))
        queries = [query + ';' for query in queries]

        return queries
