from django.shortcuts import render
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def admin_login_page(request):
    template_name = 'dashboard_site/index.html'
    return render(request, template_name, {})
