#!/usr/bin/python3
"""Starting my first Flask web app"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays 'Hello HBNB!' at the root on 0.0.0.0 port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays 'HBNB' at /hbnb on 0.0.0.0 port 5000"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
