from django import template

register = template.Library()

@register.filter(name="get_value")
def get_value(dict : dict, key):
    if key in dict:
        return dict[key]
    else:
        return '<undefined>'