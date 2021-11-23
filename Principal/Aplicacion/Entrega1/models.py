from typing import Match
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.db.models.fields.related import ForeignKey


class player(models.Model):
    Nickname = models.CharField(max_length=25, verbose_name="Nickname", blank=False, null=False)
    Password = models.CharField(max_length=50, verbose_name="Password", blank=False, null=False)
    email = models.EmailField(verbose_name="Email", blank=False, null=False)

    #def __str__(self):
    #    return self.Nickname

class hero(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False)
    rareza = CharField(max_length=15, verbose_name="Rareza", blank=False, null=False)
    imagen = CharField(max_length=100, verbose_name="Imagen", blank=False, null=False)

    def __str__(self):
        return self.Nombre

class card(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False)
    Tipo = models.CharField(max_length=20, verbose_name="Tipo", blank=False, null=False)
    Valor = models.IntegerField(verbose_name="Valor", blank=False, null=False)
    imagen = CharField(max_length=100, verbose_name="Imagen", blank=False, null=False)

    def __str__(self):
        return self.Nombre

class coleccionHeroe(models.Model):
    ID_player = ForeignKey(player, on_delete=models.CASCADE, blank=False, null=False)
    ID_Hero = ForeignKey(hero, on_delete=models.CASCADE, blank=False, null=False)
