#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages containing PII
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated by replacing specified field values
    with a redaction string.

    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string to replace field values with
        message: string representing the log line
        separator: character separating fields in the log line

    Returns:
        The obfuscated log message
    """
    for field in fields:
        message = re.sub(
            f'{field}=.*?{separator}',
            f'{field}={redaction}{separator}',
            message)
    return message
