import typing

__all__ = [
    'ValidationError',
]


class ValidationError(Exception):
    """Init custom validate data error."""
    def __init__(self, data: typing.Dict, message: str = 'Invalid data.'):
        self.message = message
        self.data = data

    def __repr__(self) -> str:
        return '<ValidationError [message={}, data={}]>'.format(
            self.message, self.data)
