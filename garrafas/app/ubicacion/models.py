from django.db import models
from django.db.models.deletion import CASCADE, PROTECT


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


def __str__(self):
    return self.nombre


class Meta:
    db_table = 'depto'
    verbose_name = 'Departamento'
    verbose_name_plural = 'Departamentos'
    ordering = ['id']


class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_depto = models.ForeignKey(Departamento, on_delete=models.PROTECT)


def __str__(self):
    return self.nombre


class Meta:
    db_table = 'dist'
    verbose_name = 'Distrito'
    verbose_name_plural = 'Distritos'
    ordering = ['id']
