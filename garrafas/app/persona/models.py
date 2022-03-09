from garrafaweb.settings import MEDIA_URL, STATIC_URL
from ubicacion.models import Departamento, Distrito
from django.db import models
from datetime import datetime

from django.forms.models import model_to_dict


# Create your models here.
# from django.forms import model_to_dict
# from garrafaweb.config.settings import MEDIA_URL, STATIC_URL


class Vulnerabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    tipov = models.CharField(max_length=50, verbose_name='Tipo de Vulnerabilidad')
    baja = models.BooleanField(default=True)

    def __str__(self):
        return self.tipov

    class Meta:
        db_table = 'vulnerabilidad'
        verbose_name = 'Vulnerabilidad'
        verbose_name_plural = 'Vulnerabilidades'
        ordering = ['id']


class TipoDni(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_dni = models.CharField(max_length=50, verbose_name='Tipo de Documento')
    baja = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo_dni

    class Meta:
        db_table = 'tipo_dni'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'
        ordering = ['id']


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre/s')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    nro_dni = models.CharField(max_length=11, unique=True, verbose_name='N° Documento')
    vulneracion = models.ForeignKey(Vulnerabilidad, on_delete=models.PROTECT, verbose_name='Vulneracion')
    tipodocumento = models.ForeignKey(TipoDni, on_delete=models.PROTECT, verbose_name='Tipo de Documento')
    departamento_id = models.PositiveIntegerField(verbose_name='Departamento')
    distrito_id = models.PositiveIntegerField(verbose_name='Distrito')
    calle = models.CharField(max_length=50, verbose_name='Calle', null=True)
    nro_calle = models.PositiveIntegerField(verbose_name='Calle Nro')
    obs = models.TextField(verbose_name='Observaciones', null=True)
    fecharegistro = models.DateField(default=datetime.now, null=True)
    fechacreacion = models.DateTimeField(auto_now=True, null=True)
    fechaactualiza = models.DateField(auto_now_add=True, null=True)
    # salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    usuario_id = models.PositiveIntegerField(default=0, verbose_name='usuario_id', null=True)
    # imgdni = models.ImageField(upload_to='imgdni/%Y/%m/%d', null=True, blank=True, verbose_name='Fotocopia DNI')
    imgdni_front = models.ImageField(upload_to='imgdni_front/%Y/%m/%d', null=True, blank=True, verbose_name='Frente DNI')
    imgdni_back = models.ImageField(upload_to='imgdni_back/%Y/%m/%d', null=True, blank=True, verbose_name='Dorso DNI')
    # nanses = models.ImageField(upload_to='nanses/%Y/%m/%d', null=True, blank=True, verbose_name='Negativa - Anses')
    baja = models.BooleanField(default=True)
    # id_puntoencuentro = models.ManyToManyField(verbose_name='Punto de Encuentro')
    # cantrecargas = models.PositiveIntegerField(verbose_name='Cantidad de Recargas', default=0)

    def __str__(self):
        return self.id

    def get_image1(self):
        if self.imgdni_front:
            return '{}{}'.format(MEDIA_URL, self.imgdni_front)
        return '{}{}'.format(STATIC_URL, 'img/camera_slash.png')
    
    def get_image2(self):
        if self.imgdni_back:
            return '{}{}'.format(MEDIA_URL, self.imgdni_back)
        return '{}{}'.format(STATIC_URL, 'img/camera_slash.png')
        
        

    def toJSON(self):
        item = model_to_dict(self, exclude=['usuario_id'])
        # item = {'id': self.id, 'nombre': self.nombre}
        return item

    class Meta:
        db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']


class PersonaPuntoDeEncuentro(models.Model):
    id = models.AutoField(primary_key=True)
    id_puntoe = models.PositiveIntegerField(verbose_name='Punto Encuentro')
    id_persona = models.PositiveIntegerField(verbose_name='Persona')

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'persona_puntoe'
        verbose_name = 'PersonaPuntoe'
        ordering = ['id']
