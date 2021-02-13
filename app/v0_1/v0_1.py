from flask import Blueprint
from flask_restful import Api
import app.v0_1.models.services as services

# Create the API V1 blueprint
v0_1_blueprint = Blueprint("v0_1", __name__)

# Generate a Flask API from the blueprint
v0_1_api = Api(v0_1_blueprint)


# Define API Routes
v0_1_api.add_resource(services.Services, "/<string:lang>/services")
v0_1_api.add_resource(services.Service, "/<string:lang>/service/<string:identifier>")
