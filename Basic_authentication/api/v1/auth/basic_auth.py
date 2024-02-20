#!/usr/bin/env python3
""" Module for basic auth
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
from models.base import DATA


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ function that extract Authorization value from header request
        """
        if (authorization_header is None or
            not isinstance(authorization_header, str) or
                authorization_header[:6] != 'Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ function that decodes a value of Base64
        """
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_auth = base64.b64decode(base64_authorization_header)
            return decoded_auth.decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """ Function that extractu user crednential from a decoded
            authorization header
        """
        if (decoded_base64_authorization_header is None or
            not isinstance(decoded_base64_authorization_header, str) or
                ':' not in decoded_base64_authorization_header):
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """ Function that retrieve an user based on the credentials
        """
        if (user_email is None or
                not isinstance(user_email, str) or
                user_pwd is None or
                not isinstance(user_pwd, str)):
            return None
        if DATA == {}:
            return None
        user = User.search({'email': user_email})[0]
        if not user:
            return None
        if user.is_valid_password(user_pwd):
            return user
