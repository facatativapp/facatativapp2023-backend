import os

import cloudinary.models
from django.db import transaction
from slugify import slugify

tiposInmueble = [
    {
        "id": 1,
        "nombre": "Apartamentos",
        "icono": "iconos/apartamentos.png",
        "foto": "backgrounds/apartmentos.jpg",
    },
    {
        "id": 2,
        "nombre": "Casas",
        "icono": "iconos/casas.png",
        "foto": "backgrounds/casas.jpg",
    },
    {
        "id": 3,
        "nombre": "Fincas",
        "icono": "iconos/fincas.png",
        "foto": "backgrounds/fincas.jpg",
    },
    {
        "id": 4,
        "nombre": "Oficinas / Locales",
        "icono": "iconos/oficina.png",
        "foto": "backgrounds/oficina.jpg",
    },
    {
        "id": 5,
        "nombre": "Lotes / Predios",
        "icono": "iconos/lotes.png",
        "foto": "backgrounds/lotes.jpg",
    },
    {
        "id": 6,
        "nombre": "Otros",
        "icono": "iconos/otros-inmobiliaria.png",
        "foto": "backgrounds/otros-inmobiliaria.jpg",
    },
]


def crear_datos_iniciales_inmobiliaria(apps, schema_editor):
    with transaction.atomic():
        # Crear tipos de inmueble
        TipoInmueble = apps.get_model("inmobiliaria", "TipoInmueble")
        prefijo = "assets/inmobiliaria/"
        for tipo in tiposInmueble:
            foto = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + tipo["foto"],
                folder="inmobiliaria/fotos/",
                public_id=tipo["foto"].split(".")[0],
            )
            icono = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + tipo["icono"],
                folder="inmobiliaria/iconos/",
                public_id=tipo["icono"].split(".")[0],
            )
            nuevo_tipo_inmueble = TipoInmueble()
            nuevo_tipo_inmueble.id = tipo["id"]
            nuevo_tipo_inmueble.nombre = tipo["nombre"]
            nuevo_tipo_inmueble.foto = foto["secure_url"]
            nuevo_tipo_inmueble.icono = icono["secure_url"]
            nuevo_tipo_inmueble.slug = slugify(tipo["nombre"])
            nuevo_tipo_inmueble.save()
