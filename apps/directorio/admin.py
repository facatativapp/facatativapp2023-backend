from django.contrib import admin

from .models import Establecimiento, FotoEstablecimiento

# Register your models here.


class EstablecimientoAdmin(admin.ModelAdmin):
    exclude = ["slug"]


admin.site.register(Establecimiento, EstablecimientoAdmin)
admin.site.register(FotoEstablecimiento)
