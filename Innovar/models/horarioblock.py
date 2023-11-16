from django.db import models

class HorariosBloqueados(models.Model):
    Horario = models.DateField()

    def __str__(self):
        return self.Horario
    
    class Meta:
        verbose_name_plural = "Horarios_Bloqueados"