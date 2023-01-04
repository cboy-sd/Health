from django import template
import urllib.parse as urlparse
from urllib.parse import urlencode

register = template.Library()


@register.filter
def process_full_path(value):
    url_parts = list(urlparse.urlparse(value))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    # print(query)
    if 'page' in query:
        del query['page']
    # print(query)
    return '?' + urlencode(query) + '&'
