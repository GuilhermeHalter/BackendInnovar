from rest_framework.serializers import ModelSerializer

from Innovar.models import Procedimentos

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimentos
        fields = "__all__"