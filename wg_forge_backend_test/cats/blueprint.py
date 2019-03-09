"""Define blueprint for cats sub-package."""
import flask

__all__ = ['cats_blueprint']


cats_blueprint = flask.Blueprint(
    'cats', __name__,
)
