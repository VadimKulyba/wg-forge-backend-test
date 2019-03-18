"""This views contain cats views"""
import logging
import typing

import flask

from flask import request
from werkzeug.exceptions import BadRequestKeyError
from sqlalchemy import desc, asc
from sqlalchemy import orm, ext

from IPython import embed

from .. import errors
from .. import extensions

from ..conf import Config
from ..extensions import limiter
from ..views import create_instance

from .models import Cat
from .schemas import cats_schema, cat_schema
from .blueprint import cats_blueprint


__all__ = [
    'ping',
    'index',
    'create',
]

ORDER_OPTIONS = ['desc', 'asc']

logger = logging.getLogger('wg_forge_backend_test.cats.views')


def request_params(name: str):
    try:
        data = request.args[name]
    except BadRequestKeyError:
        return ({
            "status": 400,
            "message": "can not get {} form input data".format(name)
        })
    return data


def request_order_by(
    model: ext.declarative.api.DeclarativeMeta,
    relation: orm.query.Query
) -> orm.query.Query:
    request_attribute = request_params('attribute')
    request_order = request_params('order')

    source = None
    for column in model.__table__.columns:
        if str(column).split('.')[-1] == request_attribute:
            source = eval(model.__name__ + '.' + request_attribute)

    if type(request_order) == dict and source is not None:
        return relation.order_by(source)

    if request_order in ORDER_OPTIONS and source is not None:
        order_direction = eval('{}({})'.format(request_order, source))
        return relation.order_by(order_direction)

    return relation


def request_limit(relation: orm.query.Query) -> orm.query.Query:
    request_limit = request_params('limit')

    if type(request_limit) != dict:
        return relation.limit(request_limit)

    return relation


def request_offset(relation: orm.query.Query) -> orm.query.Query:
    request_offset = request_params('offset')

    if type(request_offset) != dict:
        return relation.offset(request_offset)

    return relation


@cats_blueprint.route('/ping')
def ping() -> typing.Tuple[flask.Response, int]:
    return flask.jsonify("Cats Service. Version 0.1"), 200


@limiter.limit("{}/{}".format(Config.REQUEST_LIMIT, Config.REQUEST_LIMIT_FORMAT))
@cats_blueprint.route('/cats', methods=['GET'])
def index() -> typing.Tuple[flask.Response, int]:
    ordered_relation = request_order_by(Cat, Cat.query)
    offseted_relation = request_offset(ordered_relation)
    limitted_relation = request_limit(offseted_relation)
    result_relation = limitted_relation.all()

    result = cats_schema.dump(result_relation)
    return flask.jsonify(result.data)


@cats_blueprint.route('/cat', methods=['POST'])
def create() -> typing.Tuple[flask.Response, int]:
    """Push new cat in database."""

    logger.debug("Start post request to '/cats'")

    try:
        cat = create_instance(cat_schema, flask.request.form.to_dict(), extensions.database.session)
        logger.debug('Cat with name {!r} successfully created'.format(cat.name))
    except errors.ValidationDataError as e:
        logger.error("Request form is invalid: {!r}".format(e))
        return flask.jsonify(**e.data), 400
    except Exception as e:
        logger.error("Cat not saving.")
        logger.exception(e)
        raise

    return flask.jsonify(details=['OK']), 201
