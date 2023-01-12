from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce

from django.contrib.auth import get_user_model

User = get_user_model()


class WeekDay:
    SAT = 'السبت'
    SUN = 'الاحد'
    MON = 'الاثنين'
    TUE = 'الثلاثاء'
    WED = 'الاربعاء'
    THU = 'الخميس'
    FRI = 'الجمعه'

    CHOICES = (

        (SAT, 'السبت'),
        (SUN, 'الاحد'),
        (MON, 'الاثنين'),
        (TUE, 'الثلاثاء'),
        (WED, 'الاربعاء'),
        (THU, 'الخميس'),
        (FRI, 'الجمعه'),
    )


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=150, blank=True)
    hospital = models.CharField(max_length=256, blank=True)
    bank_account_type = models.CharField(max_length=100, blank=True)
    bank_account = models.CharField(max_length=100, blank=True)
    appointment_cost = models.FloatField()
    healthcare_cost = models.FloatField()
    is_active = models.BooleanField(default=True)
    # timestamp
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def full_name(self, *args, **kwargs):
        return self.user.full_name

    @property
    def phone_number(self, *args, **kwargs):
        return self.user.phone_number

    @property
    def gender(self, *args, **kwargs):
        return self.user.gender

    def __str__(self):
        return f"{self.user.full_name}"


class DoctorTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    days = models.CharField(
        max_length=255,
        choices=WeekDay.CHOICES,
        default=WeekDay.SAT
    )
    day_order = models.IntegerField(default=1, editable=False)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = [
            'day_order',
            'start_hour'
        ]

    def save(self, *args, **kwargs):
        self.day_order = WeekDay.CHOICES.index((self.days, self.days))
        super(DoctorTime, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.days} - {self.start_hour} - {self.end_hour}"


class DoctorExperience(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    experience = models.TextField()
