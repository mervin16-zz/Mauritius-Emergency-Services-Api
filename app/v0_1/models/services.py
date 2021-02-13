from flask_restful import Resource
import json
from app.messages.messages import Message

# A list of the available json file in each language mapping its path
json_file = {
    "en": "app/v0_2/data/services_en.json",
    "fr": "app/v0_2/data/services_fr.json",
}
# The default path if language doesn't math any of them
json_def = "data/services_en.json"

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
                return (
                    Message.content_not_found(),
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
                Message.content_services(services),
                200,
            )  # 200 OK HTTP VERB
