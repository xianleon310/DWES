from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Juego, Equipo, Torneo, Jugador, Participacion
from .serializers import (
    JuegoSerializer, EquipoSerializer, TorneoSerializer,
    JugadorSerializer, ParticipacionSerializer
)
from .filters import TorneoFilter, EquipoFilter, JugadorFilter


class JuegoViewSet(ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['genero']
    search_fields = ['nombre', 'desarrollador']
    ordering_fields = ['nombre', 'created_at']
    ordering = ['nombre']


class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EquipoFilter
    search_fields = ['nombre', 'tag', 'pais']
    ordering_fields = ['nombre', 'created_at', 'activo']
    ordering = ['-created_at']


class TorneoViewSet(ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TorneoFilter
    search_fields = ['nombre', 'descripcion', 'ubicacion']
    ordering_fields = ['nombre', 'premio_total', 'created_at', 'max_equipos']
    ordering = ['-created_at']


class JugadorViewSet(ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JugadorFilter
    search_fields = ['nickname', 'pais']
    ordering_fields = ['nickname', 'rango_actual', 'created_at']
    ordering = ['-rango_actual', 'nickname']


class ParticipacionViewSet(ModelViewSet):
    queryset = Participacion.objects.all()
    serializer_class = ParticipacionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['equipo_id', 'torneo_id', 'posicion_final']
    ordering_fields = ['posicion_final', 'premio_ganado', 'fecha_inscripcion']
    ordering = ['posicion_final']