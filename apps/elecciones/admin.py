from django.contrib import admin

from .models import Candidato, Candidatura, Partido

# Register your models here.

admin.site.register(Candidato)
admin.site.register(Candidatura)
admin.site.register(Partido)
