#!/usr/bin/env python3
""" Entry point
"""
from flask import Flask, jsonify, request, abort, make_response, redirect

from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def test() -> str:
    """ Route to test the server
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """ Route to resgister an user
    """
    try:
        AUTH.register_user(request.form['email'], request.form['password'])
        return jsonify(
            {
                "email": f"{request.form['email']}",
                "message": "user created"
            }
        )
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """ Route to login
    """
    if (AUTH.valid_login(request.form['email'], request.form['password'])):
        session_id = AUTH.create_session(request.form['email'])
        resp_message = jsonify(
            {"email": request.form['email'], "message": "logged in"})
        resp = make_response(resp_message)
        resp.set_cookie('session_id', session_id)
        return resp
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ Route to logout
    """
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect("/")
    except Exception:
        abort(403)


@app.route('/profile')
def profile():
    """ Route to get users's profile
    """
    try:
        session_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(session_id)
        return jsonify({"email": user.email})

    except Exception:
        abort(403)


@app.route('rest_password', methods=['POST'])
def get_reset_password_token():
    """ Route for reset password
    """
    email = request.form['email']
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return ({"email": email, "reset_token": reset_token})

    except Exception:
        abort(403)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
