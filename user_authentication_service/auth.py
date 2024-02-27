#!/usr/bin/env python3
""" Authentificate module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Method that hashes password using bcrypt
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if the password matches with the email
        """
        try:
            user = self._db.find_user_by(email=email)
            return (
                bcrypt.checkpw(bytes(password, 'utf-8'),
                               user.hashed_password)
            )
        except NoResultFound:
            return False
