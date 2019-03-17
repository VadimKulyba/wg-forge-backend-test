"""This modele contain cat models schemas."""
import typing

import marshmallow.fields
import marshmallow.validate
from marshmallow import validates, validates_schema

from .. import schemas
from .. import errors
from . import models

__all__ = [
    'CatSchema',
    'cat_schema',
    'cats_schema',
]


class CatSchema(schemas.BaseSchema):
    """Schema for cat model."""
    MIN_SIZE = 1

    name = marshmallow.fields.String(
        required=True, validate=marshmallow.validate.Length(min=3))
    color = marshmallow.fields.String(required=False)
    tail_length = marshmallow.fields.Integer(required=False)
    whiskers_length = marshmallow.fields.Integer(required=False)

    @validates_schema
    def validate_size(self, data):
        if data['tail_length'] < self.MIN_SIZE:
            raise errors.ValidationDataError(data, 'Small tail_length size validation error.')
        if data['whiskers_length'] < self.MIN_SIZE:
            raise errors.ValidationDataError(data, 'Small whiskers_length size validation error.')

    @validates('color')
    def validate_color(self, data):
        if data not in models.COLOR_TUPLE:
            raise errors.ValidationDataError(data, 'Validation error, not supported color type.')

    class Meta(schemas.BaseSchema.Meta):
        """Cat's schema meta class."""
        model = models.Cat


cat_schema = CatSchema()
cats_schema = CatSchema(many=True)
