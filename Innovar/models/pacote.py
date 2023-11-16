from django.db import models
from rest_framework.serializers import SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

class Pacote(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Pacotes"