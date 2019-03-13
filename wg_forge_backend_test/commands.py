from flask_script import Command

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from collections import Counter
from statistics import median

from .conf import Config
from .services import ColorStatisticCollector, CatStatisticCalculator
from .cats.models import Cat, CatColorInfo, CatStatistic


class DatabaseFiller(Command):
    """Fill empty tables."""
    def run(self):
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        self.session = Session(engine)
        self.write_color_statistic()
        self.write_cat_statistic()
        self.session.close()

    def write_color_statistic(self):
        ColorStatisticCollector(self.session).call()

    def write_cat_statistic(self):
        CatStatisticCalculator(self.session).call()
