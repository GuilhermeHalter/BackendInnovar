from rest_framework.viewsets import ModelViewSet

from Innovar.models import Pacote
from Innovar.serializers import PacoteSerializer

class PacoteViewSet(ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer