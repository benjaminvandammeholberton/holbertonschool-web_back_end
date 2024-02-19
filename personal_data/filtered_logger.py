#!/usr/bin/env python3
"""
Logging module
"""
import logging
import re
from typing import List
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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
    logger = logging.getLogger('user_data')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function taht create mysql connection"""
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.environ.get("PERSONAL_DATA_DB_NAME")

    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host, database=database)
    return cnx


def main():
    """"""
    db = get_db()
    logger = get_logger()
    if db and db.is_connected():
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM users ;")
            rows = cursor.fetchall()
            for row in rows:
                message = (
                    f"name={row[0]}; "
                    f"email={row[1]}; "
                    f"phone={row[2]}; "
                    f"ssn={row[3]}; "
                    f"password={row[4]}; "
                    f"ip={row[5]}; "
                    f"last_origin={row[6]}; "
                    f"user_agent={row[7]};"
                )
                logger.info(message)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
