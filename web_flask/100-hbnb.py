#!/usr/bin/python3
"""Starting Flask web app"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage


app = Flask(__name__)


app.static_folder = 'static'
app.static_url_path = '/static'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display a HTML page like Airbnb states and amenities
    on 0.0.0.0 port 5000
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', state=states, am=amenities, place=places)


@app.teardown_appcontext
def close_session(exception):
    """closes a sqlalchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
