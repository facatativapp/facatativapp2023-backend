from django.urls import path

from .api import get_inmueble, get_inmuebles, get_tipos_inmueble

urlpatterns = [
    path("get_tipos_inmueble/<str:tipo>", get_tipos_inmueble),
    path("get_inmuebles/<str:tipo>", get_inmuebles),
    path("get_inmueble/<str:inmueble>", get_inmueble),
]
