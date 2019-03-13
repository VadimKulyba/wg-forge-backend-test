"""Project servuces container."""
from sqlalchemy import func
from collections import Counter
from statistics import median

from IPython import embed

from .cats.models import Cat, CatColorInfo, CatStatistic

__all__ = [
    'ColorStatisticCollector',
    'CatStatisticCalculator',
]


class ColorStatisticCollector():
    """Collect or update statistic."""
    def __init__(self, session):
        self.session = session

    def call(self):
        color_info = self.session.query(
            func.count(Cat.color),
            Cat.color).group_by(Cat.color).all()
        for count, color in color_info:
            relation = CatColorInfo.query.filter_by(color=color)
            if relation.count() > 0:
                relation.first().count = count
            else:
                info = CatColorInfo(color=color, count=count)
                self.session.add(info)
        self.session.commit()
        self.session.close()


class CatStatisticCalculator():
    """Control service for cat statistic."""
    def __init__(self, session):
        self.session = session

    def call(self):
        statistic_relation = CatStatistic.query
        if statistic_relation.count() > 0:
            self.attach_params(statistic_relation.first())
        else:
            statistic = self.attach_params(CatColorInfo())
            self.session.add(statistic)
        self.session.commit()
        self.session.close()

    def attach_params(self, obj):
        """Add params on relation before save."""
        obj.tail_length_mean = self.custom_mean_calculator(Cat.tail_length)
        obj.tail_length_median = self.custom_median_calculator(Cat.tail_length)
        obj.tail_length_mode = self.multi_mode(self.items)
        obj.whiskers_length_mean = self.custom_mean_calculator(Cat.whiskers_length)
        obj.whiskers_length_median = self.custom_median_calculator(Cat.whiskers_length)
        obj.whiskers_length_mode = self.multi_mode(self.items)
        return obj

    def custom_mean_calculator(self, resource) -> float:
        sql_util_obj = self.session.query(func.avg(resource)).all()
        return float(sql_util_obj[0][0])

    def custom_median_calculator(self, resource):
        objects = self.session.query(resource).all()
        self.items = [item[0] for item in objects if item[0] is not None]
        return median(self.items)

    def multi_mode(self, items) -> tuple:
        """seach all mode with equal count."""
        dictionary = dict(Counter(items))
        max_value = max(dictionary.values())

        result_list = []
        for key, value in dictionary.items():
            if value == max_value:
                result_list.append(key)

        return tuple(result_list)
