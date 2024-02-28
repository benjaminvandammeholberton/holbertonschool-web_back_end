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
        """ Create user session and return session ID
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Get an user based on the session_id cookie
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user

        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a user's session
        """
        try:
            self._db.update_user(user_id, session_id=None)
            return None

        except Exception:
            raise

    def get_reset_password_token(self, email: str) -> str:
        """ Generates reset password token
        """
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                raise ValueError
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token

        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update the user's password
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, reset_token=None,
                                 hashed_password=hashed_password)

        except Exception:
            ValueError

        return None
