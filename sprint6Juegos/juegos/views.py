from rest_framework.viewsets import ModelViewSet
from .models import Juego, Equipo, Torneo,Jugador,Participacion
from .serializers import JuegoSerializer, EquipoSerializer, TorneoSerializer,JugadorSerializer,ParticipacionSerializer

class JuegoViewSet(ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class TorneoViewSet(ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

class JugadorViewSet(ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class ParticipacionViewSet(ModelViewSet):
    queryset = Participacion.objects.all()
    serializer_class = ParticipacionSerializer