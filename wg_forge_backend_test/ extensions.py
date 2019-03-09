"""Contains of flask extensions."""
import flasgger
import flask_migrate
import flask_sqlalchemy

__all__ = [
    'database',
    'migrate',
    'swagger',
]

database = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
swagger = flasgger.Swagger()
