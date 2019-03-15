"""This modele contain cat models schemas."""
import typing

import marshmallow.fields
import marshmallow.validate

from .. import schemas
from . import models

__all__ = [
    'CatSchema',
]


class CatSchema(schemas.BaseSchema):
    """Schema for cat model."""

    name = marshmallow.fields.String(required=True)
    color = marshmallow.fields.String(required=False)
    tail_length = marshmallow.fields.Float(required=False)
    whiskers_length = marshmallow.fields.Float(required=False)

    class Meta(schemas.BaseSchema.Meta):
        """Cat's schema meta class."""
        model = models.Cat
