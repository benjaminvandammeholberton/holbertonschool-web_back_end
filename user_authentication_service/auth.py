#!/usr/bin/env python3
""" Authentificate module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Method that hashes password using bcrypt
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
