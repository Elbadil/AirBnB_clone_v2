#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    displays number at /number/<n> on 0.0.0.0 port 5000
    only if n is number
    """
    return "{} is a number".format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    displays a HTML page at /number_template/<n> on 0.0.0.0
    port 5000 only if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
