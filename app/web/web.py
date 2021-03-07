from flask import Blueprint, render_template as HTML, redirect

# Create the API V1 blueprint
web = Blueprint("web", __name__, static_folder="static", template_folder="templates")


######################################
############# Main Pages #############
######################################

@web.route("/")
def home_view():
    return HTML("index.html")

@web.route("/privacy")
def privacy_view():
    return HTML("privacy.html")

