from django.urls import path

from .api import get_candidato, get_candidatos, get_candidaturas

urlpatterns = [
    path("get_candidaturas", get_candidaturas),
    path("get_candidatos/<int:candidatura>", get_candidatos),
    path("get_candidato/<int:candidato>", get_candidato),
]
