from django.db import models

class HorariosBloqueados(models.Model):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.data} - {self.hora_inicio} até {self.hora_fim}"


    
    