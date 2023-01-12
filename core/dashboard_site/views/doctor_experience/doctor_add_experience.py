from django.shortcuts import render, redirect, reverse
from core.doctor.models import Doctor, DoctorExperience
from core.doctor.forms import DoctorExperienceForm
from ....doctor.models import DoctorTime, Doctor, DoctorExperience
from django.db import transaction
from django.contrib import messages


def doctor_add_experience(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    template_name = "dashboard_site/doctor/doctor_experience_add.html"
    if request.method == "POST":

        data = dict(request.POST.items())

        experience_data = {
            'experience': data.get('experience'),
            'doctor': doctor.pk
        }
        print(experience_data)
        with transaction.atomic():

            form = DoctorExperienceForm(experience_data)
            if form.is_valid():
                messages.success(request, f'لقد إضافة  الخبره بنجاح')
                print(f'form is valid {form.data}')
                form.save()
                print(f' form is saved with data {form.data}')
                return redirect(
                    reverse('dashboard_site:doctor_details', kwargs={"doctor_id": doctor.pk})
                )
                print("view redirected")
            else:
                messages.error(request, f'هناك بعض الاخطاء عليك الانتباه لها')
                return render(request, template_name, {
                    'doctor_id': doctor.pk,
                    "form": form
                })

    return render(request, template_name, {
        "doctor_id": doctor.pk
    })
