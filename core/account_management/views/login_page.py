from django.shortcuts import render
from django.contrib.auth import login, logout

from ..models import User


def home(request):
    template_name = 'account/login.html'

    return render(request, template_name, context=None)


def user_login(request):
    if request.method == 'POST':
        template_name = "account/login.html"
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            login(request, user)
        except:
            print("sorry invalid user data !!!")
            render(request, template_name)
