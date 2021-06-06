from flask import Flask
import googlemaps

# Creating our flask app
app = Flask(__name__)

# Creatinf googlemaps API client
gmaps = googlemaps.Client(key='enter your key here')

from geoapp import routes
