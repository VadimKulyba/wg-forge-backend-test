"""Define invalid data error for schemas."""
import typing

__all__ = [
    'ValidationDataError',
]


class ValidationDataError(Exception):
    """Init custom validate data error."""
    def __init__(self, data: typing.Dict, message: str = 'Invalid data.'):
        self.message = message
        self.data = data

    def __repr__(self) -> str:
        return '<ValidationDataError [message={}, data={}]>'.format(
            self.message, self.data)
