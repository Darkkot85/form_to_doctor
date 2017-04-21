from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'doctor', 'date', 'time']
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}