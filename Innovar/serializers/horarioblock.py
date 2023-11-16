from rest_framework.serializers import ModelSerializer

from Innovar.models import HorariosBloqueados

class HorariosBloqueadoSerializer(ModelSerializer):
    class Meta:
        model = HorariosBloqueados
        fields = "__all__"