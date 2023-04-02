import os

import cloudinary.models
from django.db import transaction
from slugify import slugify

categoriasEstablecimiento = [
    {
        "id": 1,
        "nombre": "Lugares de Interés",
        "icono": "iconos/lugares-interes.png",
        "foto": "backgrounds/lugares-interes.jpg",
    },
    {
        "id": 2,
        "nombre": "Restaurantes",
        "icono": "iconos/restaurantes.png",
        "foto": "backgrounds/restaurantes.jpg",
    },
    {
        "id": 3,
        "nombre": "Alojamiento",
        "icono": "iconos/alojamiento.png",
        "foto": "backgrounds/alojamiento.jpg",
    },
    {
        "id": 4,
        "nombre": "Shopping",
        "icono": "iconos/shopping.png",
        "foto": "backgrounds/shopping.jpg",
    },
    {
        "id": 5,
        "nombre": "Ocio",
        "icono": "iconos/ocio.png",
        "foto": "backgrounds/ocio.jpg",
    },
    {
        "id": 6,
        "nombre": "Hogar",
        "icono": "iconos/hogar.png",
        "foto": "backgrounds/hogar.jpg",
    },
    {
        "id": 7,
        "nombre": "Educación",
        "icono": "iconos/educacion.png",
        "foto": "backgrounds/educacion.jpg",
    },
    {
        "id": 8,
        "nombre": "Salud",
        "icono": "iconos/salud.png",
        "foto": "backgrounds/salud.jpg",
    },
    {
        "id": 9,
        "nombre": "Víveres",
        "icono": "iconos/viveres.png",
        "foto": "backgrounds/viveres.jpg",
    },
    {
        "id": 10,
        "nombre": "Deportes",
        "icono": "iconos/deportes.png",
        "foto": "backgrounds/deportes.jpg",
    },
    {
        "id": 11,
        "nombre": "Servicios Profesionales",
        "icono": "iconos/servicios-profesionales.png",
        "foto": "backgrounds/servicios-profesionales.jpg",
    },
    {
        "id": 12,
        "nombre": "Servicios de Emergencia",
        "icono": "iconos/servicios-emergencia.png",
        "foto": "backgrounds/servicios-emergencia.jpg",
    },
]

subcategoriasEstablecimiento = [
    {
        "id": 1,
        "nombre": "Parques",
        "icono": "iconos/parques.png",
        "foto": "backgrounds/parques.jpg",
        "categoria": 1,
    },
    {
        "id": 2,
        "nombre": "Cultural",
        "icono": "iconos/cultura.png",
        "foto": "backgrounds/cultural.jpg",
        "categoria": 1,
    },
    {
        "id": 3,
        "nombre": "Iglesias",
        "icono": "iconos/iglesia.png",
        "foto": "backgrounds/iglesias.jpg",
        "categoria": 1,
    },
    {
        "id": 4,
        "nombre": "Institucional",
        "icono": "iconos/institucional.png",
        "foto": "backgrounds/institucional.jpg",
        "categoria": 1,
    },
    {
        "id": 5,
        "nombre": "Escenarios Deportivos",
        "icono": "iconos/escenarios-deportivos.png",
        "foto": "backgrounds/escenarios-deportivos.jpg",
        "categoria": 1,
    },
    {
        "id": 6,
        "nombre": "Asaderos",
        "icono": "iconos/asaderos.png",
        "foto": "backgrounds/asaderos.jpg",
        "categoria": 2,
    },
    {
        "id": 7,
        "nombre": "Casual / Tradicional",
        "icono": "iconos/tradicional.png",
        "foto": "backgrounds/tradicional.jpg",
        "categoria": 2,
    },
    {
        "id": 8,
        "nombre": "Carnes",
        "icono": "iconos/carnes.png",
        "foto": "backgrounds/carnes.jpg",
        "categoria": 2,
    },
    {
        "id": 9,
        "nombre": "Comida de Mar",
        "icono": "iconos/comida-de-mar.png",
        "foto": "backgrounds/comida-de-mar.jpg",
        "categoria": 2,
    },
    {
        "id": 10,
        "nombre": "Comida Asiática",
        "icono": "iconos/comida-asiatica.png",
        "foto": "backgrounds/comida-asiatica.jpg",
        "categoria": 2,
    },
    {
        "id": 11,
        "nombre": "Comida Mexicana",
        "icono": "iconos/comida-mexicana.png",
        "foto": "backgrounds/comida-mexicana.jpg",
        "categoria": 2,
    },
    {
        "id": 12,
        "nombre": "Comidas Rápidas",
        "icono": "iconos/comida-rapida.png",
        "foto": "backgrounds/comidas-rapidas.jpg",
        "categoria": 2,
    },
    {
        "id": 13,
        "nombre": "Helados y Postres",
        "icono": "iconos/helados.png",
        "foto": "backgrounds/helados-postres.jpg",
        "categoria": 2,
    },
    {
        "id": 14,
        "nombre": "Hoteles",
        "icono": "iconos/hotel.png",
        "foto": "backgrounds/hoteles.jpg",
        "categoria": 3,
    },
    {
        "id": 15,
        "nombre": "Renta Vacacional",
        "icono": "iconos/renta-vacacional.png",
        "foto": "backgrounds/renta-vacacional.jpg",
        "categoria": 3,
    },
    {
        "id": 16,
        "nombre": "Artesanías",
        "icono": "iconos/artesanias.png",
        "foto": "backgrounds/artesanias.jpg",
        "categoria": 4,
    },
    {
        "id": 17,
        "nombre": "Bolsos y Accesorios",
        "icono": "iconos/bolsos.png",
        "foto": "backgrounds/bolsos.jpg",
        "categoria": 4,
    },
    {
        "id": 18,
        "nombre": "Centros Comerciales",
        "icono": "iconos/centros-comerciales.png",
        "foto": "backgrounds/centro-comercial.jpg",
        "categoria": 4,
    },
    {
        "id": 19,
        "nombre": "Ropa",
        "icono": "iconos/ropa.png",
        "foto": "backgrounds/ropa.jpg",
        "categoria": 4,
    },
    {
        "id": 20,
        "nombre": "Zapatos",
        "icono": "iconos/zapatos.png",
        "foto": "backgrounds/zapatos.jpg",
        "categoria": 4,
    },
    {
        "id": 21,
        "nombre": "Bares",
        "icono": "iconos/bares.png",
        "foto": "backgrounds/bar.jpg",
        "categoria": 5,
    },
    {
        "id": 22,
        "nombre": "Cafés",
        "icono": "iconos/cafe.png",
        "foto": "backgrounds/cafe.jpg",
        "categoria": 5,
    },
    {
        "id": 23,
        "nombre": "Cines",
        "icono": "iconos/cine.png",
        "foto": "backgrounds/cine.jpg",
        "categoria": 5,
    },
    {
        "id": 24,
        "nombre": "Discotecas",
        "icono": "iconos/discoteca.png",
        "foto": "backgrounds/discoteca.jpg",
        "categoria": 5,
    },
    {
        "id": 25,
        "nombre": "Licores",
        "icono": "iconos/licores.png",
        "foto": "backgrounds/licores.jpg",
        "categoria": 5,
    },
    {
        "id": 26,
        "nombre": "Tecnología",
        "icono": "iconos/tecnologia.png",
        "foto": "backgrounds/tecnologia.jpg",
        "categoria": 6,
    },
    {
        "id": 27,
        "nombre": "Electrodomésticos",
        "icono": "iconos/electrodomesticos.png",
        "foto": "backgrounds/electrodomesticos.jpg",
        "categoria": 6,
    },
    {
        "id": 28,
        "nombre": "Muebles",
        "icono": "iconos/muebles.png",
        "foto": "backgrounds/muebles.jpg",
        "categoria": 6,
    },
    {
        "id": 29,
        "nombre": "Pisos y Cerámicas",
        "icono": "iconos/pisos.png",
        "foto": "backgrounds/pisos.jpg",
        "categoria": 6,
    },
    {
        "id": 30,
        "nombre": "Mascotas",
        "icono": "iconos/mascotas.png",
        "foto": "backgrounds/mascotas.jpg",
        "categoria": 6,
    },
    {
        "id": 31,
        "nombre": "Papelerías y Misceláneas",
        "icono": "iconos/papeleria.png",
        "foto": "backgrounds/papeleria.jpg",
        "categoria": 6,
    },
    {
        "id": 32,
        "nombre": "Colegios",
        "icono": "iconos/colegio.png",
        "foto": "backgrounds/colegio.jpg",
        "categoria": 7,
    },
    {
        "id": 33,
        "nombre": "Universidades",
        "icono": "iconos/universidad.png",
        "foto": "backgrounds/universidad.jpg",
        "categoria": 7,
    },
    {
        "id": 34,
        "nombre": "Jardines Infantiles",
        "icono": "iconos/jardines-infantiles.png",
        "foto": "backgrounds/jardines-infantiles.jpg",
        "categoria": 7,
    },
    {
        "id": 35,
        "nombre": "Idiomas",
        "icono": "iconos/idiomas.png",
        "foto": "backgrounds/idiomas.jpg",
        "categoria": 7,
    },
    {
        "id": 36,
        "nombre": "Otros",
        "icono": "iconos/otros-educacion.png",
        "foto": "backgrounds/conduccion.jpg",
        "categoria": 7,
    },
    {
        "id": 37,
        "nombre": "Clínicas y Hospitales",
        "icono": "iconos/hospital.png",
        "foto": "backgrounds/clinica.jpg",
        "categoria": 8,
    },
    {
        "id": 38,
        "nombre": "Farmacias",
        "icono": "iconos/farmacia.png",
        "foto": "backgrounds/farmacia.jpg",
        "categoria": 8,
    },
    {
        "id": 39,
        "nombre": "Salud Dental",
        "icono": "iconos/dentista.png",
        "foto": "backgrounds/salud-dental.jpg",
        "categoria": 8,
    },
    {
        "id": 40,
        "nombre": "Ópticas",
        "icono": "iconos/gafas.png",
        "foto": "backgrounds/opticas.jpg",
        "categoria": 8,
    },
    {
        "id": 41,
        "nombre": "Supermercados",
        "icono": "iconos/supermercado.png",
        "foto": "backgrounds/supermercado.jpg",
        "categoria": 9,
    },
    {
        "id": 42,
        "nombre": "Carnes y Pollo",
        "icono": "iconos/viveres-carnes.png",
        "foto": "backgrounds/viveres-carnes.jpg",
        "categoria": 9,
    },
    {
        "id": 43,
        "nombre": "Salsamentaria y Víveres",
        "icono": "iconos/salsamentaria.png",
        "foto": "backgrounds/viveres.jpg",
        "categoria": 9,
    },
    {
        "id": 44,
        "nombre": "Fútbol 5",
        "icono": "iconos/futbol.png",
        "foto": "backgrounds/futbol5.jpg",
        "categoria": 10,
    },
    {
        "id": 45,
        "nombre": "Gimnasios",
        "icono": "iconos/gimnasio.png",
        "foto": "backgrounds/gimnasio.jpg",
        "categoria": 10,
    },
    {
        "id": 46,
        "nombre": "Ciclismo",
        "icono": "iconos/ciclismo.png",
        "foto": "backgrounds/ciclismo.jpg",
        "categoria": 10,
    },
    {
        "id": 47,
        "nombre": "Bancos / Cajeros",
        "icono": "iconos/bancos.png",
        "foto": "backgrounds/cajero.jpg",
        "categoria": 11,
    },
    {
        "id": 48,
        "nombre": "Lavanderías",
        "icono": "iconos/lavanderia.png",
        "foto": "backgrounds/lavanderia.jpg",
        "categoria": 11,
    },
    {
        "id": 49,
        "nombre": "Transporte",
        "icono": "iconos/transporte.png",
        "foto": "backgrounds/transporte.jpg",
        "categoria": 11,
    },
    {
        "id": 50,
        "nombre": "Parqueaderos",
        "icono": "iconos/parqueadero.png",
        "foto": "backgrounds/parqueadero.jpg",
        "categoria": 11,
    },
    {
        "id": 51,
        "nombre": "Veterinarias",
        "icono": "iconos/veterinaria.png",
        "foto": "backgrounds/veterinaria.jpg",
        "categoria": 11,
    },
    {
        "id": 52,
        "nombre": "Otros Servicios Profesionales",
        "icono": "iconos/documento-legal.png",
        "foto": "backgrounds/contaduria.jpg",
        "categoria": 11,
    },
    {
        "id": 53,
        "nombre": "Policía",
        "icono": "iconos/policia.png",
        "foto": "backgrounds/policia.jpg",
        "categoria": 12,
    },
    {
        "id": 54,
        "nombre": "Desastres",
        "icono": "iconos/ambulancia.png",
        "foto": "backgrounds/emergencia.jpg",
        "categoria": 12,
    },
]


def crear_datos_iniciales_directorio(apps, schema_editor):
    with transaction.atomic():
        # Crear categorias de establecimientos
        CategoriaEstablecimiento = apps.get_model(
            "directorio", "CategoriaEstablecimiento"
        )
        prefijo = "assets/directorio/"
        for categoria in categoriasEstablecimiento:
            foto = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + categoria["foto"],
                folder="directorio/fotos/",
                public_id=categoria["foto"].split(".")[0],
            )
            icono = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + categoria["icono"],
                folder="directorio/iconos/",
                public_id=categoria["icono"].split(".")[0],
            )
            nuevo_tipo_inmueble = CategoriaEstablecimiento()
            nuevo_tipo_inmueble.id = categoria["id"]
            nuevo_tipo_inmueble.nombre = categoria["nombre"]
            nuevo_tipo_inmueble.foto = foto["secure_url"]
            nuevo_tipo_inmueble.icono = icono["secure_url"]
            nuevo_tipo_inmueble.slug = slugify(categoria["nombre"])
            nuevo_tipo_inmueble.save()
        # Crear subcategorias de establecimientos
        SubcategoriaEstablecimiento = apps.get_model(
            "directorio", "SubcategoriaEstablecimiento"
        )
        prefijo = "assets/directorio/"
        for subcategoria in subcategoriasEstablecimiento:
            foto = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + subcategoria["foto"],
                folder="directorio/fotos/",
                public_id=subcategoria["foto"].split(".")[0],
            )
            icono = cloudinary.uploader.upload(
                os.path.dirname(prefijo) + "/" + subcategoria["icono"],
                folder="directorio/iconos/",
                public_id=subcategoria["icono"].split(".")[0],
            )
            nuevo_tipo_inmueble = SubcategoriaEstablecimiento()
            nuevo_tipo_inmueble.id = subcategoria["id"]
            nuevo_tipo_inmueble.nombre = subcategoria["nombre"]
            nuevo_tipo_inmueble.foto = foto["secure_url"]
            nuevo_tipo_inmueble.icono = icono["secure_url"]
            nuevo_tipo_inmueble.slug = slugify(subcategoria["nombre"])
            nuevo_tipo_inmueble.categoria_id = subcategoria["categoria"]
            nuevo_tipo_inmueble.save()
