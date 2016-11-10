from datetime import date


class Date(object):

    """
    represents a date.
    attributes: month, day, year
    """


def current_weekday():
    a = date.today()
    print a.strftime('%A')

current_weekday()


d = Date()
d.month = 11
d.day = 11
d.year = 2016


def print_date(date):

    print('{}.{}.{}'.format(date.month, date.day, date.year))



print_date(d)
