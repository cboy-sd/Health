from django.shortcuts import render


def admin_dashboard(request):
    template_name = 'dashboard_site/admin_dashboard.html'
    context = {
        "doctor_count": 0,
        "patient_count": 0,
        "incoming_appointment_count": 0,
        "total_balance": 0,
        "appointment": None,

    }
    return render(request, template_name, context=context)
