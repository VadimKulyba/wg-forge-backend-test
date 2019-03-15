import typing

import marshmallow_sqlalchemy
import sqlalchemy.orm.session

from .errors import ValidationError
from .extensions import database

__all__ = [
    'BaseSchema',
]


class BaseSchema(marshmallow_sqlalchemy.ModelSchema):
    """Base schema for project.
    This schema already contains a database session instance.
    """

    class Meta:
        """Predefine schema with session"""
        sql_session: sqlalchemy.orm.session.Session = database.session

    def validate(
        self,
        data: typing.Dict,
        session: sqlalchemy.orm.session.Session = None,
        *args,
        **kwargs,
    ) -> None:
        """Raises of data invalid. ???"""
        validation_data = super().validate(
            data, session=session, *args, **kwargs)
        if validation_data:
            raise ValidationError(validation_data)
        return None
