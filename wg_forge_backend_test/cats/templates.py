"""Any render json status templates."""
import flask

from .blueprint import cats_blueprint


@cats_blueprint.errorhandler(429)
def ratelimit_handler(error):
    return flask.jsonify("429 Too Many Requests"), 429
