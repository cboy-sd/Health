from django.contrib.auth.decorators import login_required
from ..models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


@login_required
def delete_user_page(request):
    user = User.objects.get(user_name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirmation')
