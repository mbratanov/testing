# forms.py
from django import forms
from .models import ScheduleInterval


class ScheduleIntervalForm(forms.ModelForm):
    class Meta:
        model = ScheduleInterval
        exclude = ['schedule']
