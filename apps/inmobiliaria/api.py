from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import FotoInmueble, Inmueble, TipoInmueble


@api_view(["GET"])
@permission_classes([AllowAny])
def get_tipos_inmueble(request, tipo=None):
    if tipo == "all":
        tipos = TipoInmueble.objects.all().order_by("nombre").values()
    if tipo == "featured":
        slugs = ["apartamentos", "casas", "fincas", "oficinas-locales"]
        tipos = TipoInmueble.objects.filter(slug__in=slugs).order_by("nombre").values()
    response = []
    for tipo in tipos:
        new_tipo = {
            "id": tipo["id"],
            "nombre": tipo["nombre"],
            "slug": tipo["slug"],
            "foto": tipo["foto"].url,
            "icono": tipo["icono"].url,
        }
        response.append(new_tipo)
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_inmuebles(request, tipo):
    tipo = TipoInmueble.objects.get(slug=tipo)
    new_tipo = {"nombre": tipo.nombre, "slug": tipo.slug}
    inmuebles = (
        Inmueble.objects.filter(Q(tipo=tipo) & Q(activo=True))
        .order_by("-promocionado")
        .values()
    )
    new_inmuebles = []
    for inmueble in inmuebles:
        new_inmueble = {
            "id": inmueble["id"],
            "slug": inmueble["slug"],
            "foto": inmueble["foto"].url,
            "barrio": inmueble["barrio"],
        }
        new_inmuebles.append(new_inmueble)
    response = {"tipo": new_tipo, "inmuebles": new_inmuebles}
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_inmueble(request, inmueble):
    inmueble = Inmueble.objects.get(slug=inmueble)
    fotos = FotoInmueble.objects.filter(inmueble=inmueble).values()
    new_fotos = [inmueble.foto.url]
    for foto in fotos:
        new_fotos.append(foto["foto"].url)
    inmueble = {
        "barrio": inmueble.barrio,
        "direccion": inmueble.direccion,
        "latitud": inmueble.latitud,
        "longitud": inmueble.longitud,
        "precioVenta": inmueble.precioVenta,
        "precioArriendo": inmueble.precioArriendo,
        "numeroHabitaciones": inmueble.numeroHabitaciones,
        "numeroBanios": inmueble.numeroBanios,
        "capacidadPersonas": inmueble.capacidadPersonas,
        "area": inmueble.area,
        "descripcion": inmueble.descripcion,
        "telefono": inmueble.telefono,
        "email": inmueble.email,
        "tipo": {
            "nombre": inmueble.tipo.nombre,
            "slug": inmueble.tipo.slug,
        },
        "fotos": new_fotos,
    }
    return Response(inmueble)
