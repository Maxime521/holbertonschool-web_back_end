#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages containing PII
"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Redact sensitive fields in log message before formatting
        """
        message = record.getMessage()
        record.msg = filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Get a logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FLIELDS))
    logger.addHandler(handler)
    return logger
