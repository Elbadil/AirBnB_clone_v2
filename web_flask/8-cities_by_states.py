#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    displays a HTML page at /cities_by_states on 0.0.0.0
    port 5000 and diplays states id and name and also cities names
    and ids of each state
    """
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def close_session(exception):
    """closes a sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
