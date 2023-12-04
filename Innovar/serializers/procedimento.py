from rest_framework.serializers import ModelSerializer, SlugRelatedField

from Innovar.models import Procedimentos

from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProcedimentoSerializer(ModelSerializer):
    cover_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Procedimentos
        fields = "__all__"