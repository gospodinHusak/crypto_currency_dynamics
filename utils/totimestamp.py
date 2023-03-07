from datetime import datetime, date, timezone, time


def totimestamp(dt):
    year, month, day = list(map(int, dt.split('-')))
    todatetime = datetime.combine(date(year, month, day), time(0, 0))
    return int(todatetime.replace(tzinfo=timezone.utc).timestamp() * 1000)