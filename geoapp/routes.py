from flask import request
from flask_expects_json import expects_json
from geoapp import app
from geoapp.geolocation import get_location
from geoapp.input_validation import schema

@app.errorhandler(400)
def bad_request(e):
    return {"description" : "Check the json payload"}, 400

@app.route("/getAddressDetails", methods=["POST"])
@expects_json(schema)
def receiver():
    # Returns coordinates and address in Json/XML
    data = request.json
    response = get_location(data)
    return response, 200