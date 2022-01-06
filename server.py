

from flask import Flask
from mock_data import catalog
import json

# new instance of Flask class
app = Flask("__name__")

me = {
            "name": "Eric",
            "last": "Moore",
            "age:": 35,
            "hobbies":[],
            "address":{
                "street": "Evergreen",
                "number": 42,
                "city": "SpringField"

                }
    }


@app.route("/", methods=['GET'])
def home():
    return "Hello from Python"


@app.route("/test")
def any_name():
    return "I'm a test function"


@app.route("/about")
def my_name():
    return (me["name"] + " " + me["last"])


# *******************************************************************************
# ********************************** API ENDPOINTS ******************************
# *******************************************************************************

@app.route("/api/catalog")
def get_catalog():
    # TODO:read the catalog from a database

    return json.dumps(catalog)


@app.route("/api/cheapest")
def get_cheapest():
    # find the chepest product on the catalog list
    # 1 - travel the list (catalog) for loop
    # 2 - print the price on the consol

    cheap = catalog[0]
    for product in catalog:
        if product["price"] < cheap["price"]:
            cheap = product

    #return it as json
    return json.dumps(cheap)



@app.route("/api/product/<id>")
def get_product(id):
    # find the product whos _id is equal to id
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)
            
    #return it as json
    return "NOT FOUND"
# start the server
app.run(debug=True)