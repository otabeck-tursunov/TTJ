from django.db import models


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Viloyat(CoreModel):
    TURI = (
        ('shahar', 'shahar'),
        ('viloyat', 'viloyat'),
    )

    nom = models.CharField(max_length=255)
    turi = models.CharField(max_length=20, choices=TURI)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'

    def __str__(self):
        return self.nom


class Tuman(CoreModel):
    TURI = (
        ('shahar', 'shahar'),
        ('tuman', 'tuman'),
    )

    nom = models.CharField(max_length=255)
    turi = models.CharField(max_length=20, choices=TURI)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tuman'
        verbose_name_plural = 'Tumanlar'

    def __str__(self):
        return self.nom


class Fakultet(CoreModel):
    nom = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = 'Fakultetlar'

    def __str__(self):
        return self.nom
