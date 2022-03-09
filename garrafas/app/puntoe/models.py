from django.db import models
from datetime import datetime

from django.db.models.deletion import PROTECT


class Puntoe(models.Model):
    id = models.AutoField(primary_key=True)
    nombrepe = models.CharField(max_length=50)
    id_depto = models.PositiveIntegerField(default=0)
    id_distrito = models.PositiveIntegerField(default=0)
    calle = models.CharField(max_length=50)
    nro_calle = models.PositiveIntegerField(default=0)
    nombre_ambito = models.CharField(max_length=50)
    manzana_ambito = models.CharField(max_length=50)
    casa_ambito = models.CharField(max_length=50)
    fecharegistro = models.DateField(default=datetime.now)
    fechape = models.DateTimeField(auto_now=True)
    fechaactualiza = models.DateField(auto_now_add=True)
    baja = models.BooleanField(default=True)
    id_usuario_baja = models.CharField(max_length=50)
    # id_persona = models.ManyToManyField(Persona)


def __str__(self):
    return self.nombrepe


class Meta:
    db_table = 'puntoe'
    verbose_name = 'Punto de Encuentro'
    verbose_name_plural = 'Puntos de Encuentro'
    ordering = ['id']
