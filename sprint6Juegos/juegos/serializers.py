from rest_framework import serializers
from .models import Juego, Equipo, Torneo

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id', 'nombre', 'genero', 'desarrollador', 
        'imagen_portada', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'tag', 'logo', 'pais', 'jugador_id', 
        'activo', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'descripcion', 'juego_id',
        'premio_total', 'modalidad', 'max_equipos', 'estado', 
        'ubicacion', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }