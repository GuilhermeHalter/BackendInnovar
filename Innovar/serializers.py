from rest_framework.serializers import ModelSerializer

from Innovar.models import Pacote

class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = "__all__"