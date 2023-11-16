from django.contrib import admin

from .models import Procedimentos, HorariosBloqueados, Pacote

admin.site.register(Pacote)
admin.site.register(Procedimentos)
admin.site.register(HorariosBloqueados)
