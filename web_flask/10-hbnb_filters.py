#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage


app = Flask(__name__)


app.static_folder = 'static'
app.static_url_path = '/static'


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    display a HTML page like 6-index.html on 0.0.0.0
    port 5000
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', state=states, am=amenities)


@app.teardown_appcontext
def close_session(exception):
    """closes a sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
