import datetime
import re

from django import template
from datetime import datetime as dt


register = template.Library()


@register.filter(name="format_date")
def format_date(value):
    if type(value) is not float:
        return value

    date = datetime.datetime.fromtimestamp(value, datetime.UTC)
    now = dt.now(datetime.UTC)
    diff = now - date
    if diff.seconds / 60 < 10:
        return "только что"
    elif diff.days < 1:
        return f'{int(diff.seconds / 60 / 60)} часов назад'
    else:
        return date.strftime("%Y-%m-%d")

@register.filter(name="score")
def score(value):
    if type(value) is str:
        return value

    if type(value) is int:
        if value < -5:
            return "плохо"
        elif value > 5:
            return "хорошо"
        elif value >= -5 and value <= 5:
            return "нейтрально"

    return value


@register.filter
def format_num_comments(value):
    if type(value) is int:
        if value == 0:
            return "Оставьте комментарий"
        elif value < 50:
            return value
        elif value > 50:
            return "50+"

@register.filter
def format_selftext(value, count):
    stub_body = " ... "
    pattern = r"[\s]+"
    matches = list(re.finditer(pattern, value, re.M))

    if len(matches) < (count * 2) + len(stub_body):
        return value
    else:
        start_part = value[:matches[count].regs[0][0]]
        end_part = value[matches[-count].regs[0][1]:]
        return f'{start_part}{stub_body}{end_part}'