from django.urls import path, include
from .views.admin_dashboard import admin_dashboard
from .views.doctor_management.doctor_list import doctor_list
from .views.doctor_management.doctor_detail import doctor_details
from .views.doctor_management.edit_doctor import edit_doctor_page
from .views.doctor_experience.delet_doctor_experience import delete_doctor_experience
from .views.doctor_experience.doctor_edit_experience import doctor_experience_edit_page
from .views.doctor_experience.doctor_add_experience import doctor_add_experience

app_name = 'dashboard_site'

urlpatterns = [
    path(
        '', admin_dashboard,
        name='dashboard'),
    # doctor
    path(
        'doctor/',
        doctor_list,
        name='doctor_list'
    ),

    path(
        'doctor_details/<int:doctor_id>',
        doctor_details,
        name='doctor_details'
    ),
    path(
        'edit_doctor_page/<int:doctor_id>',
        edit_doctor_page,
        name='edit_doctor_page'
    ),
    path(
        'delete_doctor_experience/',
        delete_doctor_experience,
        name='delete_doctor_experience'
    ),
    path(
        'doctor/edit/<int:doctor_id>/experience/<int:experience_id>/',
        doctor_experience_edit_page,
        name='doctor_experience_edit_page'
    ),
    path(
        'doctor/details/add_experience/<int:doctor_id>/',
        doctor_add_experience,
        name='doctor_add_experience'
    )
]
