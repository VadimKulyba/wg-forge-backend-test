import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        os.getenv("POSTGRES_USER", "wg_forge"),
        os.getenv("POSTGRES_PASSWORD", "42a"),
        os.getenv("POSTGRES_HOST", "localhost"),
        os.getenv("POSTGRES_PORT", "5434"),
        os.getenv("POSTGRES_DB", "wg_forge_db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PACKAGE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    MIGRATIONS_DIRECTORY = os.path.join(PACKAGE_DIRECTORY, 'migrations')

    REQUEST_LIMIT = 1
    REQUEST_LIMIT_FORMAT = 'minute'
