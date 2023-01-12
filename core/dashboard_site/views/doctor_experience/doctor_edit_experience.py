from django.db import transaction
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import redirect
from django.contrib import messages
from core.doctor.models import Doctor, DoctorExperience
from core.doctor.forms import DoctorExperienceForm
from core.security.route_security import staff_required


@staff_required
def doctor_experience_edit_page(request, doctor_id, experience_id):
    template_name = 'dashboard_site/doctor/doctor_experience_edit.html'

    doctor = Doctor.objects.get(pk=doctor_id)
    doctor_experience = DoctorExperience.objects.get(pk=experience_id)

    if request.method == 'POST':

        # TODO: Check that the user haven't already bought the course

        data = dict(request.POST.items())

        with transaction.atomic():

            experience_data = {
                'doctor': doctor.pk,
                'experience': data.get('experience'),
            }

            form = DoctorExperienceForm(
                experience_data,
                instance=doctor_experience
            )

            if form.is_valid():

                form.save()

                messages.success(request, f'تم تعديل الخبره بنجاح')
                messages.success(request, f'if you are still breathong there is a hope ')
                return redirect(
                    reverse('dashboard_site:doctor_details', kwargs={"doctor_id": doctor.pk})
                )

            else:
                messages.error(request, f'هناك بعض الاخطاء عليك الانتباه لها')
                messages.error(request, f'if you are still breathong there is a hope ')

                return render(request, template_name, {
                    'doctor': doctor,
                    'doctor_experience': doctor_experience,
                    "form": form
                })

    return render(request, template_name, {
        'doctor': doctor,
        'doctor_experience': doctor_experience,
    })