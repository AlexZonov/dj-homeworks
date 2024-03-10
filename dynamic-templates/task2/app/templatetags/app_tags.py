from django import template


register = template.Library()

@register.filter(name='is_active')
def is_active_filter(value, arg):
    if value == arg:
        return "active"
    else:
        return ""