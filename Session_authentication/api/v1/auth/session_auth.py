#!/usr/bin/env python3
""" Module for session auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ SessionAuth class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None):
        """ Creates a session
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        id = str(uuid4())
        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return an user id based on the session id
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)
