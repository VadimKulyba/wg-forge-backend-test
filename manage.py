import flask_script

from wg_forge_backend_test import create_application
from wg_forge_backend_test.extensions import database
from wg_forge_backend_test.cats import models
from wg_forge_backend_test.commands import DatabaseFiller
from wg_forge_backend_test.conf import Config

manager = flask_script.Manager(create_application)
manager.add_command("runserver", flask_script.Server())
manager.add_command("shell", flask_script.Shell())
manager.add_command("fill_database", DatabaseFiller())


@manager.shell
def make_shell_context():
    return dict(
        app=create_application(), 
        config=Config, 
        db=database, 
        models=models)


def main():
    manager.run()


if __name__ == '__main__':
    main()
