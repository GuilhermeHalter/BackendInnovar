from django.contrib import admin

from .models import Pacote, Procedimentos, HorariosBloqueados

admin.site.register(Pacote)
admin.site.register(Procedimentos)
admin.site.register(HorariosBloqueados)
