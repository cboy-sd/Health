# import json
# from operator import attrgetter
from functools import wraps
from django.shortcuts import reverse
from django.shortcuts import redirect
# from django.utils.http import urlencode
# from pprint import pprint


def login_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        print(request)
        if request.user.is_authenticated:
            return f(request, *args, **kwargs)
        return redirect(reverse('dashboard_site:admin-login-page', kwargs={'next': request.url}))

    return wrapper


"""
return redirect(
    reverse('dashboard_site:admin-login-page') + '?' + urlencode({'next': request.path})
)
"""


def staff_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return f(request, *args, **kwargs)
        return redirect(reverse('dashboard_site:admin-login-page'))

    return wrapper


def superuser_required(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return f(request, *args, **kwargs)
        return redirect(reverse('dashboard_site:admin-login-page'))

    return wrapper
