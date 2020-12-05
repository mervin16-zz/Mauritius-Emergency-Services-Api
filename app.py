from flask import Flask
from flask_restful import Api
from messages.messages import Message
from models.services import Service, Services

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


api.add_resource(Services, "/<string:lang>/services")
api.add_resource(Service, "/<string:lang>/service/<string:identifier>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
