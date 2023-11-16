from rest_framework.viewsets import ModelViewSet

from Innovar.models import Pacote, Procedimentos
from Innovar.serializers import PacoteSerializer, ProcedimentoSerializer

class PacoteViewSet(ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer

class ProcedimentoViewSet(ModelViewSet):
    queryset = Procedimentos.objects.all()
    serializer_class = ProcedimentoSerializer
