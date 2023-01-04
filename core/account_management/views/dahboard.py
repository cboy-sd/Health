from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def user_dashboard(request):
    return render(request,
                  'account/user/dashboard.html',
                  {'section': 'profile', 'order': None})
