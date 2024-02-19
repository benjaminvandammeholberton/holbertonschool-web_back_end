#!/usr/bin/env python3
"""
Task 2 - Create logger
"""
import logging
import re
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "ip")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        pattern = rf"(?<={field}=)[^{separator}]+(?={separator})"
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Return message formated"""
        default_message = super().format(record)
        message = filter_datum(self.fields, self.REDACTION, default_message,
                               self.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """function that set a logger and return it"""
    logger = logging.getLogger = 'user_data'
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    handler.formatter(formatter)
    logger.handler(handler)
    return logger
