from rest_framework.viewsets import ModelViewSet

from Innovar.models import HorariosBloqueados
from Innovar.serializers import HorariosBloqueadoSerializer

class HorariosBloqueadoViewSet(ModelViewSet):
    queryset = HorariosBloqueados.objects.all()
    serializer_class = HorariosBloqueadoSerializer
