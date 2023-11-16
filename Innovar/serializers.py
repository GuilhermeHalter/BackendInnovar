from rest_framework.serializers import ModelSerializer

from Innovar.models import Pacote, Procedimentos

class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = "__all__"

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimentos
        fields = "__all__"