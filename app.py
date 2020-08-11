from flask import Flask, abort
from flask_restful import Resource, Api
import json

# A list of the available json file in each language mapping its path
json_file = {"en": "data/services_en.json", "fr": "data/services_fr.json"}
# The default path if language doesn't math any of them
json_def = "data/services_en.json"
# Create a Flask Application
app = Flask(__name__)
# Pass application to Api object
api = Api(app)

# Error Handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return (
        {
            "services": [],
            "message": "No services found under this identifier.",
            "success": False,
        },
        404,
    )


@app.errorhandler(400)  # Handling HTTP 400 BAD REQUEST
def page_bad_request(e):
    return (
        {
            "services": [],
            "message": "Your browser sent a request that this server could not understand.",
            "success": False,
        },
        404,
    )


# The Service class returns a single
# item from the give parameter
class Service(Resource):
    # GET Request
    def get(self, lang, identifier):
        with open(json_file.get(lang, json_def)) as services_file:
            services = json.load(services_file)
            service = next(
                filter(lambda x: x["identifier"] == identifier, services), None
            )
            if service:
                return (
                    {"services": [service], "message": "", "success": True,},
                    200,
                )
            else:
                return (
                    {
                        "services": [],
                        "message": "No services found under this identifier.",
                        "success": False,
                    },
                    404,
                )


# The Services class which returns
# a list of all available services
class Services(Resource):
    # GET Request
    def get(self, lang):
        with open(json_file.get(lang, json_def)) as services_file:
            services = json.load(services_file)
            # Returns the output in the correct format
            return (
                {"services": services, "message": "", "success": True},
                200,
            )  # 200 OK HTTP VERB


api.add_resource(Services, "/<string:lang>/services")
api.add_resource(Service, "/<string:lang>/service/<string:identifier>")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
