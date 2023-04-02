from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Candidato, Candidatura


@api_view(["GET"])
def get_candidaturas(request):
    candidaturas = Candidatura.objects.filter(activo=True).order_by("nombre").values()
    return Response(candidaturas)


@api_view(["GET"])
def get_candidatos(request, candidatura):
    candidatos = (
        Candidato.objects.select_related("partido")
        .filter(Q(activo=True) & Q(candidatura_id=candidatura))
        .order_by("-promocionado")
        .values("id", "nombre", "foto", "partido__nombre", "partido__foto")
    )
    response = []
    for candidato in candidatos:
        new_candidato = {
            "id": candidato["id"],
            "nombre": candidato["nombre"],
            "foto": candidato["foto"].url,
            "partido": candidato["partido__nombre"],
        }
        response.append(new_candidato)
    return Response(response)


@api_view(["GET"])
def get_candidato(request, candidato):
    candidato = Candidato.objects.get(id=candidato)
    response = {
        "nombre": candidato.nombre,
        "foto": candidato.foto.url,
        "email": candidato.email,
        "sitioWeb": candidato.sitioWeb,
        "telefono": candidato.telefono,
        "perfil": candidato.perfil,
        "experiencia": candidato.experiencia,
        "propuestas": candidato.propuestas,
        "numeroTarjeton": candidato.numeroTarjeton,
        "partido": candidato.partido.nombre,
    }
    return Response(response)
