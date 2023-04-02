from django.contrib import admin

from .models import FotoInmueble, Inmueble, TipoInmueble

# Register your models here.


class InmuebleAdmin(admin.ModelAdmin):
    exclude = ["slug"]


admin.site.register(FotoInmueble)
admin.site.register(Inmueble, InmuebleAdmin)
admin.site.register(TipoInmueble)
