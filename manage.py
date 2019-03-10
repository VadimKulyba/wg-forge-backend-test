import flask_script

from wg_forge_backend_test import create_application


manager = flask_script.Manager(create_application)


def main():
    manager.run()


if __name__ == '__main__':
    main()
