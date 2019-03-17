"""Contains of flask extensions."""
import flasgger
import flask_limiter
import flask_migrate
import flask_sqlalchemy


__all__ = [
    'database',
    'limiter',
    'migrate',
    'swagger',
]

database = flask_sqlalchemy.SQLAlchemy()
limiter = flask_limiter.Limiter(key_func=flask_limiter.util.get_remote_address)
migrate = flask_migrate.Migrate()
swagger = flasgger.Swagger()
