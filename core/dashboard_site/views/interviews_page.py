from django.shortcuts import render
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def interviews_page(request):
    template_name = 'dashboard_site/interviews.html'
    return render(request, template_name, {})
