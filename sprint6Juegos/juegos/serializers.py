from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Juego, Equipo, Jugador, Torneo, Participacion

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class JugadorSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    
    user_detalle = UserSerializer(
        source='user_id',
        read_only=True
    )
    
    class Meta:
        model = Jugador
        fields = ['id', 'nickname', 'user_id', 'user_detalle', 
                  'equipo_id', 'avatar', 'fecha_nacimiento', 
                  'pais', 'rango_actual', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class EquipoSerializer(serializers.ModelSerializer):
    jugadores = JugadorSerializer(many=True, read_only=True)
    jugador_id = serializers.PrimaryKeyRelatedField(
        queryset=Jugador.objects.all(),
        allow_null=True,
        required=False
    )
    
    capitan_detalle = JugadorSerializer(
        source='jugador_id',
        read_only=True
    )
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'tag', 'logo', 'pais', 'jugador_id', 
        'capitan_detalle','jugadores','activo', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class ParticipacionSerializer(serializers.ModelSerializer):
    equipo_id = serializers.PrimaryKeyRelatedField(
        queryset=Equipo.objects.all()
    )
    
    equipo_detalle = EquipoSerializer(
        source='equipo_id',
        read_only=True
    )
    
    torneo_id = serializers.PrimaryKeyRelatedField(
        queryset=Torneo.objects.all()
    )
    
    class Meta:
        model = Participacion
        fields = ['id', 'equipo_id', 'equipo_detalle', 
                  'torneo_id', 'fecha_inscripcion', 
                  'posicion_final', 'premio_ganado', 
                  'puntos_obtenidos', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class TorneoSerializer(serializers.ModelSerializer):
    
    juego_id = serializers.PrimaryKeyRelatedField(
        queryset=Juego.objects.all()
    )
    
    
    juego_detalle = JuegoSerializer(
        source='juego_id',
        read_only=True
    )

    participaciones = ParticipacionSerializer(many=True, read_only=True)

    class Meta:
        model = Torneo
        fields = ['id', 'nombre', 'descripcion', 'juego_id',
        'juego_detalle','participaciones','premio_total', 'modalidad', 'max_equipos', 
        'estado', 'ubicacion', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }