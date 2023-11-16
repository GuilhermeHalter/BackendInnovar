from rest_framework.viewsets import ModelViewSet

from Innovar.models import Pacote, Procedimentos, HorariosBloqueados
from Innovar.serializers import PacoteSerializer, ProcedimentoSerializer, HorariosBloqueadoSerializer

class PacoteViewSet(ModelViewSet):
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer

class ProcedimentoViewSet(ModelViewSet):
    queryset = Procedimentos.objects.all()
    serializer_class = ProcedimentoSerializer

class HorariosBloqueadoViewSet(ModelViewSet):
    queryset = HorariosBloqueados.objects.all()
    serializer_class = HorariosBloqueadoSerializer
