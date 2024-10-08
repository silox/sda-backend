from datetime import date

from django import template

register = template.Library()


def cut(value):
    """Removes all values of arg from the given string"""
    return value.replace('is', "")


def to_nice_date(date_param):
    """Convert date_param to friendly string representation"""

    today = date.today()
    days_num = (date_param - today).days

    if days_num == -1:
        return 'Yesterday'
    if days_num == 0:
        return 'Today'
    if days_num == 1:
        return 'Tomorrow'

    if days_num < 0:
        return f'{abs(days_num)} days ago'
    return f'In {days_num} days'


def truncate_filter(text, max_len=12):
    if max_len <= 0:
        raise ValueError('max_len must be > 0')
    if max_len <= 3:
        return text[:max_len]
    return text if len(text) <= max_len else f'{text[:max_len - 3]}...'


register.simple_tag(cut, name='cut')
register.filter("to_nice_date", to_nice_date)
register.filter('truncate', truncate_filter)
