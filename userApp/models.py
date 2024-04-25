from django.contrib.auth.models import AbstractUser
from django.db import models


class Profil(AbstractUser):
    ROLES = (
        ('admin', 'admin'),
        ('xodim', 'xodim'),
        ('nazoratchi', 'nazoratchi'),
    )

    tel = models.CharField(max_length=13)
    role = models.CharField(max_length=50, choices=ROLES)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillar"

    def __str__(self):
        return f"{self.username}: {self.role}"




