from rest_framework.viewsets import ModelViewSet
from .models import Juego, Equipo, Torneo
from .serializers import JuegoSerializer, EquipoSerializer, TorneoSerializer

class JuegoViewSet(ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class TorneoViewSet(ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer