from flask import Flask
import googlemaps

# Creating our flask app
app = Flask(__name__)

# Creatinf googlemaps API client
gmaps = googlemaps.Client(key='AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw')

from geoapp import routes