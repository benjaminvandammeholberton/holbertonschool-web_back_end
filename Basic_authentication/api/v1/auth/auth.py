#!/usr/bin/env python3
""" Module of authentification
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentification class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[len(path)-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> TypeVar('User'):
        """ Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None
        """
        return None
