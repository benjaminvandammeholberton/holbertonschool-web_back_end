#!/usr/bin/env python3
""" Entry point
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def test() -> str:
    """ Route to test the server
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
