"""Mapping cats table on cats models."""
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Numeric, Enum
from sqlalchemy.dialects import postgresql
from sqlalchemy import PrimaryKeyConstraint

from ..conf import Config

__all__ = [
    'Cat',
    'CatColorInfo',
    'CatStatistic',
]

Base = automap_base()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session = Session(engine)


COLOR_ENUM = Enum(
    'black',
    'white',
    'black & white',
    'red',
    'red & white',
    'red & black & white', 
    name="cat_color", create_type=False)


# mapped classes are now created with names by default
# matching that of the table name.
class Cat(Base):
    """Main cats model."""

    __tablename__ = 'cats'

    name = Column('name', String, primary_key=True)
    color = Column('color', COLOR_ENUM)
    tail_length = Column('tail_length', Integer)
    whiskers_length = Column('whiskers_length', Integer)


class CatColorInfo(Base):
    """Callback cats model for color info."""

    __tablename__ = 'cat_colors_info'

    color = Column('color', COLOR_ENUM)
    count = Column('count', Integer)

    __table_args__ = (
        PrimaryKeyConstraint(color, count),
    )


class CatStatistic(Base):
    """Callback cats model for statistic."""

    __tablename__ = 'cats_stat'

    tail_length_mean = Column('tail_length_mean', Numeric)
    tail_length_median = Column('tail_length_median', Numeric)
    tail_length_mode = Column(
        'tail_length_mode',
        postgresql.ARRAY(Integer, dimensions=2)
    )

    whiskers_length_mean = Column('whiskers_length_mean', Numeric)
    whiskers_length_median = Column('whiskers_length_median', Numeric)
    whiskers_length_mode = Column(
        'whiskers_length_mode',
        postgresql.ARRAY(Integer, dimensions=2)
    )

    __table_args__ = (
        PrimaryKeyConstraint(
            tail_length_mean,
            tail_length_median,
            tail_length_mode,
            whiskers_length_mean,
            whiskers_length_median,
            whiskers_length_mode),
    )


Base.prepare(engine, reflect=True)
Cat.query = session.query(Cat)
CatColorInfo.query = session.query(CatColorInfo)
CatStatistic.query = session.query(CatStatistic)
