import uuid

from cloudinary.models import CloudinaryField
from django.db import models
from slugify import slugify

# Create your models here.


class CategoriaEstablecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    icono = CloudinaryField("image", folder="directorio/iconos")
    foto = CloudinaryField("image", folder="directorio/iconos")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{}".format(self.nombre)


class SubcategoriaEstablecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    icono = CloudinaryField("image", folder="directorio/iconos")
    foto = CloudinaryField("image", folder="directorio/iconos")
    categoria = models.ForeignKey(CategoriaEstablecimiento, on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{}".format(self.nombre)


class Establecimiento(models.Model):
    # Información de Establecimiento
    nombre = models.CharField(max_length=100)
    horario = models.TextField()
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    telefono1 = models.CharField(max_length=100)
    telefono2 = models.CharField(max_length=100, null=True, blank=True)
    telefono3 = models.CharField(max_length=100, null=True, blank=True)
    sitioWeb = models.CharField(max_length=100, null=True, blank=True)
    foto = CloudinaryField("image", folder="directorio/negocios")
    activo = models.BooleanField()
    promocionado = models.BooleanField()
    slug = models.SlugField(unique=True)
    # Metadata
    fechaPublicacion = models.DateField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)
    usuario = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subcategoria = models.ManyToManyField(SubcategoriaEstablecimiento)

    def __str__(self):
        return "{}".format(self.nombre)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre + "-" + str(uuid.uuid4()).split("-")[0])
        super().save(*args, **kwargs)


class FotoEstablecimiento(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT)
    foto = CloudinaryField("image", folder="directorio/negocios")
