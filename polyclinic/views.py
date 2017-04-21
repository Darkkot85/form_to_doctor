from django.shortcuts import render
from django.views.generic import CreateView
#
# from .models import Appointment
from .forms import AppointmentForm
# Create your views  here.


class CreateAppointmentView(CreateView):
    template_name = 'appointment.html'
    form_class = AppointmentForm




