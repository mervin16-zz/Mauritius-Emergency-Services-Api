from flask import Flask
import app.v0_1.v0_1 as V0_1
import app.v0_2.v0_2 as V0_2
import app.messages.messages as MSG

# Create a Flask Application
app = Flask(__name__)

# Register Blueprints versioning
app.register_blueprint(V0_1.v0_1_blueprint, url_prefix="/v0.1")
app.register_blueprint(V0_2.v0_2_blueprint, url_prefix="/v0.2")

# Error Handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return (
        MSG.Message.CONTENT_NOT_FOUND,
        404,
    )


@app.errorhandler(400)  # Handling HTTP 400 BAD REQUEST
def page_bad_request(e):
    return (
        MSG.Message.CONTENT_BAD_REQUEST,
        404,
    )

