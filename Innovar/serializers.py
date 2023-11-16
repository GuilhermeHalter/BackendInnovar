from rest_framework.serializers import ModelSerializer

from Innovar.models import Pacote, Procedimentos, HorariosBloqueados

class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = "__all__"

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimentos
        fields = "__all__"

class HorariosBloqueadoSerializer(ModelSerializer):
    class Meta:
        model = HorariosBloqueados
        fields = "__all__"