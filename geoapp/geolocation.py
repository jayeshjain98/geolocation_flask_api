from geoapp import gmaps
import xml.etree.cElementTree as ET
from flask import json, Response
from werkzeug.exceptions import BadRequest

def json_response(address, location):
    return {
            "coordinates" : location,
            "address" : address
            }

def xml_string(lat, lng, address):
    root = ET.Element("root")
    coor = ET.SubElement(root, "coordinates")

    ET.SubElement(coor, "lat").text = lat
    ET.SubElement(coor, "lng").text = lng
    ET.SubElement(root, "address").text = address

    xml_response = ET.tostring(root, encoding='unicode', xml_declaration=True)
    return xml_response

def get_location(json_data):
    try:
        # Geocoding an address
        geocode_result = gmaps.geocode(json_data["address"])
    except:
        raise BadRequest

    # Extracting required data
    lat = str(geocode_result[0]["geometry"]["location"]["lat"])
    lng = str(geocode_result[0]["geometry"]["location"]["lng"])
    address = geocode_result[0]["formatted_address"]
    location = geocode_result[0]["geometry"]["location"]

    # Get specific response
    if json_data["output_format"].lower()=="json":
        return json_response(address, location)
    elif json_data["output_format"].lower()=="xml":
        return Response(xml_string(lat, lng, address), mimetype='text/xml')
