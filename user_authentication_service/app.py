#!/usr/bin/env python3
""" Entry point
"""
from flask import Flask, jsonify, request

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
