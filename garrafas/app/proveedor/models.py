from ubicacion.models import Departamento
from django.db import models
from datetime import datetime

from django.db.models.deletion import PROTECT


class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    nro_sidico = models.PositiveIntegerField(default=0)
    fecharegistro = models.DateField(default=datetime.now)
    fecha_expte = models.DateTimeField(auto_now=True)
    fechaactualiza = models.DateField(auto_now_add=True)
    baja = models.BooleanField(default=True)
    id_usuario_baja = models.CharField(max_length=50)
    departamento_id = models.PositiveBigIntegerField(default=0)
    # id_persona = models.ManyToManyField(Persona)


def __str__(self):
    return self.nombre


class Meta:
    db_table = 'proveedor'
    verbose_name = 'Proveedor'
    verbose_name_plural = 'Proveedores'
    ordering = ['id']
