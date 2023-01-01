from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def to_arabic_week_day(value):
    if value == 'SAT':
        return 'يوم السبت'
    elif value == 'SUN':
        return 'يوم الاحد'
    elif value == 'MON':
        return 'يوم الاثنين'
    elif value == 'TUE':
        return 'يوم الثلاثاء'
    elif value == 'WED':
        return 'يوم الاربعاء'
    elif value == 'THU':
        return 'يوم الخميس'
    elif value == 'FRI':
        return 'يوم الجمعه'
