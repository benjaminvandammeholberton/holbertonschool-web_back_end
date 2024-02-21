#!/usr/bin/env python3
""" Module of authentification
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentification class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if a given path is in the excluded paths to
            require authentification or not.
            Returns:
                - True if we need authentification
                - False if we don't
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[len(path)-1] != '/':
            path = path + '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> TypeVar('User'):
        """ Check the header of requests to get the Authorization
        """
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None

        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None
        """
        return None
