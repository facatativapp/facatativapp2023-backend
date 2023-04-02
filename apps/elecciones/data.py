from django.db import transaction
from slugify import slugify

candidaturas = [
    {"id": 1, "nombre": "Presidencia"},
    {"id": 2, "nombre": "Cámara"},
    {"id": 3, "nombre": "Senado"},
    {"id": 4, "nombre": "Gobernación"},
    {"id": 5, "nombre": "Asamblea"},
    {"id": 6, "nombre": "Alcaldía"},
    {"id": 7, "nombre": "Concejo"},
]

partidos = [
    {"id": 1, "nombre": "Partido ADA"},
    {"id": 2, "nombre": "Partido Colombia Renaciente"},
    {"id": 3, "nombre": "Partido Alianza Social Independiente ASI"},
    {"id": 4, "nombre": "Partido Alianza Verde"},
    {"id": 5, "nombre": "Partido Cambio Radical"},
    {"id": 6, "nombre": "Partido Centro Democrático"},
    {"id": 7, "nombre": "Partido Colombia Justa Libres"},
    {"id": 8, "nombre": "Partido Conservador Colombiano"},
    {"id": 9, "nombre": "Partido FARC Fuerza Alternativa Revolucionaria del Común"},
    {"id": 10, "nombre": "Partido Liberal Colombiano"},
    {"id": 11, "nombre": "Partido Político MIRA"},
    {"id": 12, "nombre": "Partido Polo Democrático Alternativo"},
    {"id": 13, "nombre": "Partido de la U"},
    {"id": 14, "nombre": "Movimiento Colombia Humana - Unión Patriótica UP"},
    {"id": 15, "nombre": "Movimiento Autoridades Indígenas de Colombia AICO"},
    {"id": 16, "nombre": "Movimiento Alternativo Indígena y Social MAIS"},
]


def crear_datos_iniciales_elecciones(apps, schema_editor):
    with transaction.atomic():
        # Crear candidaturas
        Candidatura = apps.get_model("elecciones", "Candidatura")
        for candidatura in candidaturas:
            nueva_candidatura = Candidatura()
            nueva_candidatura.id = candidatura["id"]
            nueva_candidatura.nombre = candidatura["nombre"]
            nueva_candidatura.slug = slugify(candidatura["nombre"])
            nueva_candidatura.activo = False
            nueva_candidatura.save()
        # Crear partidos
        Partido = apps.get_model("elecciones", "Partido")
        for partido in partidos:
            nuevo_partido = Partido()
            nuevo_partido.id = partido["id"]
            nuevo_partido.nombre = partido["nombre"]
            nuevo_partido.save()
