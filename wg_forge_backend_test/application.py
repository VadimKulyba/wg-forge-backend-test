import logging

import flask

from . import extensions
from .conf import Config
from .cats.blueprint import cats_blueprint

__all__ = [
    'Application',
    'create_application'
]


class Application(flask.Flask):

    @classmethod
    def create_application(
        cls,
        config: str = 'wg_forge_backend_test.conf',
        app_name: str = None
    ) -> flask.Flask:
        """Flask app builder."""
        app = cls(app_name)
        app.config.from_object(Config)
        app.config.from_object(config)
        app.extensions_fabric()
        app.blueprint_fabric()
        return app

    def blueprint_fabric(self) -> None:
        """Registration cats blueprint."""
        self.register_blueprint(
            cats_blueprint,
            url_prefix='/'
        )

    def extensions_fabric(self) -> None:
        """Load flask extension."""
        extensions.database.init_app(self)
        extensions.migrate.init_app(
            self,
            extensions.database,
            directory=self.config['MIGRATIONS_DIRECTORY'],
        )
        extensions.swagger.init_app(self)


def create_application(
    config=None,
    app_name='wg_forge_backend_test',
) -> Application:
    return Application.create_application(config=config, app_name=app_name)
