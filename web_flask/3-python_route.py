#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays 'Hello HBNB!' at the root on 0.0.0.0 port 5000"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays 'HBNB' at /hbnb on 0.0.0.0 port 5000"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays C and a text giving at /c/<text> on 0.0.0.0 port 5000"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """displays Python and a text at /python/<text> on 0.0.0.0 port 5000"""
    return "Python {}".format(escape(text).replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
