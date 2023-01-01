from django.shortcuts import render
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def admin_dashboard_page(request):
    template_name = 'dashboard_site/admin_dashboard.html'
    return render(request, template_name, {})
