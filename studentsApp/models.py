from django.db import models
from mainApp.models import *
from roomsApp.models import Joy


class Student(CoreModel):
    JINS = (
        ('erkak', 'erkak'),
        ('ayol', 'ayol')
    )

    TALIM_TURI = (
        ('kunduzgi', 'kunduzgi'),
        ('sirtqi', 'sirtqi'),
    )

    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    otasi = models.CharField(max_length=255, blank=True, null=True)
    jins = models.CharField(max_length=10, choices=JINS)
    telefon_shaxsiy = models.CharField(max_length=13)
    telefon_qoshimcha = models.CharField(max_length=13, blank=True, null=True)
    kurs = models.PositiveSmallIntegerField()
    guruh = models.CharField(max_length=10)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.SET_NULL, null=True)
    tutor = models.CharField(max_length=255)
    tuman = models.ForeignKey(Tuman, on_delete=models.SET_NULL, null=True)
    manzil = models.CharField(max_length=255)
    talim_turi = models.CharField(max_length=255, choices=TALIM_TURI)
    qarzdor = models.PositiveIntegerField(default=0)
    haqdor = models.PositiveIntegerField(default=0)
    joy = models.ForeignKey(Joy, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.otasi}"
