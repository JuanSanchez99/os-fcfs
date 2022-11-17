from flask import Blueprint

bp_api = Blueprint('api', __name__)


@bp_api.route("/")
def home():
    return "<p>Hello, World!</p>"