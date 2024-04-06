from django.core.validators import MinValueValidator
from django.db import models

from mainApp.models import CoreModel
from roomsApp.models import Joy
from studentsApp.models import Student
from userApp.models import Profil


class BandQilish(CoreModel):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    berilgan_sana = models.DateField()
    tark_etgan_sana = models.DateField(null=True)
    joy = models.ForeignKey(Joy, on_delete=models.SET_NULL, null=True)
    jami = models.FloatField(validators=[MinValueValidator(0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0)])
    qoldi = models.FloatField(validators=[MinValueValidator(0)])
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student.__str__()}: ({self.joy.xona.raqam}: {self.joy.raqam})"


class Tolov(CoreModel):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0)])
    tolangan_sana = models.DateField(null=True)
    izoh = models.TextField(null=True)
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student.__str__()}: {self.miqdor} | {self.created_at}"