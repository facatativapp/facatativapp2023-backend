from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import (
    CategoriaEstablecimiento,
    Establecimiento,
    FotoEstablecimiento,
    SubcategoriaEstablecimiento,
)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_categorias_directorio(request, tipo):
    if tipo == "all":
        categorias = CategoriaEstablecimiento.objects.all().order_by("nombre").values()
    if tipo == "featured":
        slugs = ["lugares-de-interes", "restaurantes", "alojamiento", "shopping"]
        categorias = CategoriaEstablecimiento.objects.filter(slug__in=slugs).values()
    response = []
    for categoria in categorias:
        new_categoria = {
            "id": categoria["id"],
            "slug": categoria["slug"],
            "nombre": categoria["nombre"],
            "foto": categoria["foto"].url,
            "icono": categoria["icono"].url,
        }
        response.append(new_categoria)
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_subcategorias_directorio(request, categoria):
    categoria = CategoriaEstablecimiento.objects.get(slug=categoria)
    new_categoria = {"nombre": categoria.nombre, "slug": categoria.slug}
    subcategorias = (
        SubcategoriaEstablecimiento.objects.filter(categoria=categoria)
        .order_by("nombre")
        .values()
    )
    new_subcategorias = []
    for subcategoria in subcategorias:
        new_subcategoria = {
            "id": subcategoria["id"],
            "slug": subcategoria["slug"],
            "nombre": subcategoria["nombre"],
            "foto": subcategoria["foto"].url,
            "icono": subcategoria["icono"].url,
        }
        new_subcategorias.append(new_subcategoria)
    response = {
        "categoria": new_categoria,
        "subcategorias": new_subcategorias,
    }
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_establecimientos(request, subcategoria):
    subcategoria = SubcategoriaEstablecimiento.objects.get(slug=subcategoria)
    new_subcategoria = {
        "nombre": subcategoria.nombre,
        "slug": subcategoria.slug,
        "categoria": {
            "nombre": subcategoria.categoria.nombre,
            "slug": subcategoria.categoria.slug,
        },
    }
    establecimientos = (
        Establecimiento.objects.filter(Q(subcategoria=subcategoria) & Q(activo=True))
        .order_by("-promocionado")
        .values()
    )
    new_establecimientos = []
    for establecimiento in establecimientos:
        new_establecimiento = {
            "id": establecimiento["id"],
            "nombre": establecimiento["nombre"],
            "foto": establecimiento["foto"].url,
            "direccion": establecimiento["direccion"],
            "telefono": establecimiento["direccion"],
            "slug": establecimiento["slug"],
        }
        new_establecimientos.append(new_establecimiento)
    response = {
        "subcategoria": new_subcategoria,
        "establecimientos": new_establecimientos,
    }
    return Response(response)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_establecimiento(request, establecimiento):
    establecimiento = Establecimiento.objects.get(slug=establecimiento)
    fotos = FotoEstablecimiento.objects.filter(establecimiento=establecimiento).values()
    new_fotos = [establecimiento.foto.url]
    for foto in fotos:
        new_fotos.append(foto["foto"].url)
    establecimiento = {
        "id": establecimiento.id,
        "nombre": establecimiento.nombre,
        "slug": establecimiento.slug,
        "horario": establecimiento.horario,
        "direccion": establecimiento.direccion,
        "latitud": establecimiento.latitud,
        "longitud": establecimiento.longitud,
        "descripcion": establecimiento.descripcion,
        "telefono1": establecimiento.telefono1,
        "telefono2": establecimiento.telefono2,
        "telefono3": establecimiento.telefono3,
        "sitioWeb": establecimiento.sitioWeb,
        "fotos": new_fotos,
    }
    return Response(establecimiento)
