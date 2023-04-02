from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Partido(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nombre)


class Candidatura(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return "{}".format(self.nombre)


class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    foto = CloudinaryField("image", folder="elecciones/candidatos")
    email = models.CharField(max_length=100, null=True, blank=True)
    sitioWeb = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    perfil = models.TextField(null=True, blank=True)
    experiencia = models.TextField(null=True, blank=True)
    propuestas = models.TextField(null=True, blank=True)
    numeroTarjeton = models.IntegerField(null=True, blank=True)
    partido = models.ForeignKey(Partido, on_delete=models.PROTECT)
    activo = models.BooleanField()
    promocionado = models.BooleanField()
    candidatura = models.ForeignKey(
        Candidatura, null=True, blank=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return "{}".format(self.nombre)
