from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='ФИО врача')
    def  __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Врач')
    patient_name = models.CharField(max_length=250, verbose_name='ФИО Пациента')
    date = models.DateField(verbose_name='Дата посещения')
    time = models.IntegerField(verbose_name='Назначенный час', choices=[(x, str(x)) for x in range(9,18)])






