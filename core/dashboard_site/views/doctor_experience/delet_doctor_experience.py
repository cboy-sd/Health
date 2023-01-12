from django.shortcuts import render, reverse, redirect
from django.db import transaction
from ....doctor.models import DoctorTime, Doctor, DoctorExperience
import json


def delete_doctor_experience(request):
    data = dict(request.GET.items())
    doctor_id = data.get('doctor_id')
    experience_id = data.get('experience_id')

    try:
        doctor = Doctor.objects.get(pk=data.get('doctor_id'))
        doctor_experience = DoctorExperience.objects.get(pk=data.get('experience_id'), doctor_id=doctor.pk)
        doctor_experience.delete()
        print(doctor_experience)
        return redirect(
            reverse('dashboard_site:doctor_details', kwargs={'doctor_id': doctor.pk})
        )
    except:
        return redirect(
            reverse('dashboard_site:doctor_details', kwargs={'doctor_id': doctor_id})
        )

