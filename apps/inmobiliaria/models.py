import uuid

from cloudinary.models import CloudinaryField
from django.db import models
from slugify import slugify

# Create your models here.


class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=100)
    icono = CloudinaryField("image", folder="inmobiliaria/iconos")
    foto = CloudinaryField("image", folder="inmobiliaria/backgrounds")
    slug = models.SlugField()

    def __str__(self):
        return "{}".format(self.nombre)


class Inmueble(models.Model):
    barrio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    precioVenta = models.IntegerField()
    precioArriendo = models.IntegerField()
    numeroHabitaciones = models.IntegerField()
    numeroBanios = models.IntegerField()
    capacidadPersonas = models.IntegerField()
    area = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    foto = CloudinaryField("image", folder="inmobiliaria/inmuebles")
    activo = models.BooleanField()
    promocionado = models.BooleanField()
    slug = models.SlugField()
    # Metadata
    fechaPublicacion = models.DateField(auto_now_add=True)
    fechaActualizacion = models.DateField(auto_now=True)
    usuario = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.ForeignKey(TipoInmueble, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.barrio)

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.tipo.nombre + "-" + self.barrio + "-" + str(uuid.uuid4()).split("-")[0]
        )
        super().save(*args, **kwargs)


class FotoInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.PROTECT)
    foto = CloudinaryField("image", folder="inmobiliaria")
