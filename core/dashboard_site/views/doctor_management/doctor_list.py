from django.shortcuts import render
from ....doctor.models import DoctorTime, Doctor, DoctorExperience


def doctor_list(request):
    template_name = "dashboard_site/doctor/doctors_list.html"

    return render(request, template_name, {
        "doctors": Doctor.objects.all()
    })
