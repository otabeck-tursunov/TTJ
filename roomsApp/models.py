from django.db import models
from mainApp.models import *


class Xona(CoreModel):
    raqam = models.CharField(max_length=10)
    qavat = models.PositiveSmallIntegerField()
    joylar_soni = models.PositiveSmallIntegerField()
    band = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'

    def __str__(self):
        return self.raqam


class Joy(CoreModel):
    raqam = models.CharField(max_length=3)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'

    def __str__(self):
        return f"{self.xona.raqam}: {self.raqam}"



