from django.shortcuts import render
from ....doctor.models import DoctorTime, Doctor, DoctorExperience


def doctor_details(request, doctor_id):
    template_name = "dashboard_site/doctor/doctor_details.html"
    context = {
        "total_failed_appointments": 0,
        "total_appointments": 0,
        "total_completed_appointments": 0,
        "doctor": Doctor.objects.get(pk=doctor_id),
        "doctor_times": DoctorTime.objects.filter(doctor_id=doctor_id),
        "doctor_experiences": DoctorExperience.objects.filter(doctor_id=doctor_id),
    }
    return render(request, template_name, context=context)
