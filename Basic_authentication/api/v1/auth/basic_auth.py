#!/usr/bin/env python3
""" Module for basic auth
"""
import base64
from api.v1.auth.auth import Auth


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
            return decoded_auth

        except Exception:
            return None
