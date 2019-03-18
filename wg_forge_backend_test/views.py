import typing

import flasgger
import flask_sqlalchemy
import sqlalchemy.orm.session

from .schemas import BaseSchema

__all__ = [
    'create_instance',
]


def create_instance(
    schema: BaseSchema,
    data: typing.Dict,
    session: sqlalchemy.orm.session.Session = None,
    commit: bool = True,
) -> flask_sqlalchemy.Model:
    """Validata and create model instance."""
    schema.validate(data, session=session)  # base schema
    result = schema.load(data, session=session)  # custom schema (with params)
    session = session or schema.sql_session  # check with line

    if commit:
        """Save deserialize object-data on db."""
        session.add(result.data)
        session.commit()

    return result.data


# class BaseView(flasgger.SwaggerView):
#     """Base view class."""

#     @staticmethod
#     def create_instance(
#         schema: BaseSchema,
#         data: typing.Dict,
#         session: sqlalchemy.orm.session.Session = None,
#         commit: bool = True,
#     ) -> flask_sqlalchemy.Model:
#         """Validates and creates model's instance."""
#         return create_instance(schema, data, session=session, commit=commit)
