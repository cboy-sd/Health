from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..forms import UserEditForm


@login_required()
def edit_user_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        print(user_form)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'account/user/edit_details.html', {'user_form': user_form})
