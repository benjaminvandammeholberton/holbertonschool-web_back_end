""" Module of SessionAuth views
"""
from api.v1.views import app_views

from flask import request, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    list_users = User.search({"email": email})
    if len(list_users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = list_users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response
