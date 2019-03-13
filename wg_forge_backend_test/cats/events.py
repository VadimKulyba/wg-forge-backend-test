"""listen for the 'after_insert' event"""
from sqlalchemy.orm import Session
from sqlalchemy import event

from .models import Cat, CatColorInfo
from ..services import CatStatisticCalculator


@event.listens_for(Cat, 'after_insert')
def color_info_callback(mapper, connection, instance):
    session = Session(connection)
    target_color = instance.color
    color_info_query = CatColorInfo.query.filter_by(color=target_color)
    target_count = Cat.query.filter_by(color=target_color).count() + 1
    if color_info_query.count() > 0:
        color_info_query.first().count = target_count
    else:
        session.add(CatColorInfo(color=target_color, count=target_count))
    session.commit()
    session.close()


@event.listens_for(Cat, 'after_insert')
def cat_statistic_callback(mapper, connection, instance):
    session = Session(connection)
    CatStatisticCalculator(session).call()
    session.close()
