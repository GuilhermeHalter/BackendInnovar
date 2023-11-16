from django.db import models
from rest_framework.serializers import SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

class Pacote(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Pacotes"