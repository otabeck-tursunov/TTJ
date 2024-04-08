from django.core.validators import MaxValueValidator
from django.db import models
from mainApp.models import *
from roomsApp.models import Joy
from userApp.models import Profil


class Guruh(CoreModel):
    nom = models.CharField(max_length=255)
    kurs = models.PositiveSmallIntegerField(validators=(MaxValueValidator(5),))
    fakultet = models.ForeignKey(Fakultet, on_delete=models.SET_NULL, null=True)
    tutor = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural = 'Guruhlar'

    def __str__(self):
        return self.nom


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
    imtiyozli = models.BooleanField(default=False)
    telefon_shaxsiy = models.CharField(max_length=13)
    telefon_qoshimcha = models.CharField(max_length=13, blank=True, null=True)
    guruh = models.ForeignKey(Guruh, on_delete=models.SET_NULL, null=True, blank=True)
    tuman = models.ForeignKey(Tuman, on_delete=models.SET_NULL, null=True)
    manzil = models.CharField(max_length=255)
    talim_turi = models.CharField(max_length=255, choices=TALIM_TURI)
    joy = models.ForeignKey(Joy, on_delete=models.SET_NULL, null=True, blank=True)
    balans = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.otasi}"

