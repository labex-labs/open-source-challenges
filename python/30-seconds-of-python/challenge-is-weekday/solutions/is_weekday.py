from datetime import datetime


def is_weekday(d=datetime.today()):
    return d.weekday() <= 4
