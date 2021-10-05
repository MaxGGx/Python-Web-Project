from django.db import models

class Relator(models.Model):
    nombre  = models.CharField(max_length=255, verbose_name="Nombre", blank=False, null=True)
    rut = models.CharField(max_length=11, verbose_name="Rut", blank=True, null=True)
    correo = models.CharField(max_length=60, verbose_name="Correo Electronico", blank=True, null=True)