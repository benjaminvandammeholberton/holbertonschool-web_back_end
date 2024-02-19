#!/usr/bin/env python3
"""
Task 0 - Regex-ing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        pattern = rf"(?<={field}=)[^{field}]+(?={separator})"
        message = re.sub(pattern, redaction, message)
    return message
