from django.shortcuts import render

from ..models import User
from django.shortcuts import redirect, reverse, render


def get_all_staff(request):
    if request.user.is_superuser:
        staffs = User.objects.filter(is_active=True, is_staff=True)
        context = {
            "staffs": staffs
        }
        render(request, ".html", context=context)
