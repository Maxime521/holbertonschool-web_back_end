#!/usr/bin/python3
"""
Module for filtering and obfuscating log messages containing PII
"""


import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        Returns log message with specified fields redacted.

        Args:
            fields: list of strings representing fields to obfuscate
            redaction: string to replace field values with
            message: the log line
            separator: character separating fields

        Returns:
            The obfuscated log message
    """
    for field in fields:
        message = re.sub(
            f'{field}=.*?{separator}',
            f'{field}={redaction}{separator}', message)
        return message
