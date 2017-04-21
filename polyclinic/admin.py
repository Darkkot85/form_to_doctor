from django.contrib import admin
from .models import Appointment, Doctor

class AppointmentInline(admin.TabularInline):
    model = Appointment

class DoctorAdmin(admin.ModelAdmin):
    inlines = [ AppointmentInline,]




admin.site.register(Appointment)
admin.site.register(Doctor, DoctorAdmin)
