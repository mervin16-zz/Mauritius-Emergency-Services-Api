from flask import Flask, abort
from flask_restful import Resource, Api
import json
from messages import Message

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
        Message.content_not_found(),
        404,
    )


@app.errorhandler(400)  # Handling HTTP 400 BAD REQUEST
def page_bad_request(e):
    return (
        Message.content_bad_request(),
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
                    Message.content_service(service),
                    200,
                )
            else:
                abort(404)


# The Services class which returns
# a list of all available services
class Services(Resource):
    # GET Request
    def get(self, lang):
        with open(json_file.get(lang, json_def)) as services_file:
            services = json.load(services_file)
            # Returns the output in the correct format
            return (
                Message.content_services(services),
                200,
            )  # 200 OK HTTP VERB


api.add_resource(Services, "/<string:lang>/services")
api.add_resource(Service, "/<string:lang>/service/<string:identifier>")

if __name__ == "__main__":
    app.run(port=5000)
