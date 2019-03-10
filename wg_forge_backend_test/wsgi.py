#!/usr/bin/env python3
"""Defines a gunicorn's entrpoint."""
from .application import create_application


application = create_application()


def main() -> None:
    application.run()


if __name__ == '__main__':
    main()
