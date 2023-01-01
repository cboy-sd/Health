from django.urls import path
#
from .views.admin_login_page import admin_login_page
from .views.admin_dashboard_page import admin_dashboard_page
# doctorimport doctor_time_delete_page
#
from core.dashboard_site.views.forgot_password_page import forgot_password_page
from core.dashboard_site.views.interviews_page import interviews_page

app_name = 'dashboard_site'

urlpatterns = [
    path('', admin_login_page, name='admin-login-page'),
    # admin
    path('account/forgotpassword', forgot_password_page, name='forgot_password_page'),
    # password
    path('admin/', admin_dashboard_page, name='admin_dashboard_page'),
]
