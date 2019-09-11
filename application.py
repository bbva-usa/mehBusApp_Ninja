from flask import Flask, make_response
from bson.json_util import dumps
from objs import Bus
import json
import pymongo

application = Flask(__name__)
mng_client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@testcluster0-zvzsm.mongodb.net/test?retryWrites=true&w=majority")
mng_db = mng_client["BusStops"]  # Replace mongo db name


if __name__ == "__main__":
    application.run(debug=True)

@application.route('/about')
def index():
    return "Hello, Fairfield!"


@application.route("/routes")
def get_routes():

    collection_name = 'Routes' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    return make_response(dumps(db_cm.find()))



@application.route('/buses')
def getBuses():
    return "Hello, Fairfield!"


@application.route('/buses/<busNumber>')
def getBus(busNumber):
    bus = Bus()
    return json.loads(bus.get_bus())
