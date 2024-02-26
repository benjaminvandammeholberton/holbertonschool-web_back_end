#!/usr/bin/env python3
""" Entry point
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('GET', "/")
def test():
    """ Route to test the server
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__name__':
    app.run(host="0.0.0.0", port="5000")
