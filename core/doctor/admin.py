from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *


class DoctorTimeInline(admin.StackedInline):
    model = DoctorTime
    can_delete = True
    extra = 0


class DoctorExperienceInline(admin.StackedInline):
    model = DoctorExperience
    can_delete = True
    extra = 0


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'full_name',
        'phone_number',
        'hospital',
        'specialization',
        'gender',
        'is_active',
    ]
    search_fields = ["user__full_name", "specialization", "user__phone_number"]
    list_filter = [
        'is_active',
    ]
    inlines = [DoctorTimeInline, DoctorExperienceInline]


@admin.register(DoctorTime)
class DoctorTimeAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'doctor',
        'days',
        'day_order',
        'start_hour',
        'end_hour',

    ]
    list_filter = [
        'days',
        'start_hour',
        'end_hour'
    ]
    search_fields = [
        'doctor__user__full_name',
        'doctor__user__phone_number',
    ]


@admin.register(DoctorExperience)
class DoctorExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'doctor',
        'experience',
    ]
    search_fields = [
        'doctor__user__full_name',
        'doctor__user__phone_number',
    ]
