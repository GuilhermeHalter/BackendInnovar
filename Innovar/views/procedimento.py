from rest_framework.viewsets import ModelViewSet

from Innovar.models import Procedimentos
from Innovar.serializers import ProcedimentoSerializer

class ProcedimentoViewSet(ModelViewSet):
    queryset = Procedimentos.objects.all()
    serializer_class = ProcedimentoSerializer