from django import template

register = template.Library()

@register.filter(name="color_id")
def color_filter(value):
    try:
        number = float(value)
    except ValueError:
        return ""

    if number < 0:
        return "light-green darken-3"
    elif number >= 1 and number < 2:
        return "red accent-1"
    elif number >= 2 and number < 5:
        return "red darken-1"
    elif number >= 5:
        return "red darken-4"

    return ""


@register.filter(name="value")
def value_filter(value):
    if value == "" or value is None:
        return "-"
    return value