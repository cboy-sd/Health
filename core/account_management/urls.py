from .views import dahboard, logout, login_page, delete_user, edit_details
from .forms import (PwdResetConfirmForm, PwdResetForm)
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


app_name = 'account'

urlpatterns = [
    path('dashboard', dahboard.user_dashboard, name='dashboard'),
    path('profile/edit/', edit_details.edit_user_details, name='edit_details'),
    path('profile/delete_user/', delete_user.delete_user_page, name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="account/user/delete_confirm.html"),
         name='delete_confirmation'),
]
