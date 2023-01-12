from django.shortcuts import render, redirect, reverse
from ....doctor.models import DoctorTime, Doctor, DoctorExperience
from core.security.route_security import staff_required
from core.doctor.forms import DoctorForm
from django.contrib import messages


def edit_doctor_page(request, doctor_id):
    template_name = "dashboard_site/doctor/doctor_edit.html"
    doctor = Doctor.objects.get(pk=doctor_id)

    if request.method == 'POST':
        data = dict(request.POST.items())
        # user_data = {
        #     'email': data.get('username'),
        #     'full_name': data.get('full_name'),
        #     'phone_number': data.get('phone_number_1'),
        #     'phone_number_2': data.get('phone_number_2', ''),
        #     'gender': data.get('gender', 'u'),
        # }
        doctor_data = {
            'appointment_cost': data.get('appointment_cost'),
            'healthcare_cost': data.get('healthcare_cost', doctor.espitalia_cost),
            'bank_account_type': data.get('bank_account_type', ''),
            'bank_account': data.get('bank_account', ''),
            'hospital': data.get('hospital', ''),
            'specialization': data.get('specialization', ''),
        }
        doctor_form = DoctorForm(doctor_data)
        if doctor_form.is_valid():
            doctor_form.save()

            messages.success(request, f'تمت تعديل المعلومات بنجاح')

            return redirect(
                reverse('dashboard_site:doctor_details', kwargs={'doctor_id': doctor.pk})
            )
        else:
            messages.error(request, f'هناك بعض الاخطاء عليك الانتباه لها')
            return render(request, template_name, {
                'user_form': None,
                'doctor_form': doctor,
                'doctor': doctor
            })

    return render(request, template_name, {
            "doctors": Doctor.objects.all()
        })
