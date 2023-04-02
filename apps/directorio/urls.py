from django.urls import path

from .api import (
    get_categorias_directorio,
    get_establecimiento,
    get_establecimientos,
    get_subcategorias_directorio,
)

urlpatterns = [
    path("get_categorias_directorio/<str:tipo>", get_categorias_directorio),
    path("get_subcategorias_directorio/<str:categoria>", get_subcategorias_directorio),
    path("get_establecimientos/<str:subcategoria>", get_establecimientos),
    path("get_establecimiento/<str:establecimiento>", get_establecimiento),
]
