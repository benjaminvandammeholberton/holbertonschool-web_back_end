#!/usr/bin/env python3
""" Authentificate module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ Method that hashes password using bcrypt
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generates a new uuid
    """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """
        Finds the user corresponding to the email,
        generates a new UUID and stores it in the
        database as the user's session_id.
        Returns the session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            user_id = user.id
            session_id = _generate_uuid()
            self._db.update_user(user_id, session_id=session_id)
            return session_id
        except Exception:
            return None
