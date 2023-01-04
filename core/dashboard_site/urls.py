from django.urls import path, include
from .views.admin_dashboard import admin_dashboard
from .views.doctor_views.doctor_list import doctor_list

app_name = 'dashboard_site'

urlpatterns = [
    path('', admin_dashboard, name='dashboard'),
    path('doctor/', doctor_list, name='doctor_list'),

]
