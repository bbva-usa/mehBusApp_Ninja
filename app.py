from flask import Flask, make_response
from bson.json_util import dumps
import pymongo

app = Flask(__name__)

@app.route("/routes")
def get_routes():
    mng_client = pymongo.MongoClient("mongodb+srv://admin:admin@testcluster0-zvzsm.mongodb.net/test?retryWrites=true&w=majority")
    mng_db = mng_client["BusStops"] # Replace mongo db name
    collection_name = 'Routes' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    return make_response(dumps(db_cm.find()))

if __name__ == "__main__":
    app.run(debug=True)
