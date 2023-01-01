from django import template

register = template.Library()


@register.filter
def add_to(value1, value2):
    print(value1)
    print(value2)
    return value1 + value2
