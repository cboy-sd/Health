from django.shortcuts import render

from .models import *


def all_doctors(request):
    if request.user.is_staff:
        try:
            doctors = Doctor.objects.all()
        except:
            raise Exception("sorry there is doctors!!!!")
        context = {
            "doctors": doctors
        }
        return render(request, "", context=context)


def all_patients(request):
    if request.user.is_staff:
        try:
            patients = Patient.objects.all()
        except:
            raise Exception("sorry there is patients!!!!")
        context = {
            "patients": patients
        }
        return render(request, "", context=context)


def all_orders(request):
    if request.user.is_staff:
        try:
            orders = Order.objects.all()
        except:
            raise Exception("sorry there is no  order!!!!")
        context = {
            "patients": orders
        }
        return render(request, "", context=context)


def all_orders(request):
    if request.user.is_staff:
        try:
            orders = Order.objects.all()
        except:
            raise Exception("sorry there is no  order!!!!")
        context = {
            "patients": orders
        }
        return render(request, "", context=context)
