#!/usr/bin/env python3
"""Task 10. Duck typing - first element of a sequence"""

from typing import Any, Sequence, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence,
    or None if lst is None
    """
    if lst:
        return lst[0]
    else:
        return None