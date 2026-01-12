from django.contrib import admin
from .models import Juego, Equipo, Jugador, Torneo, Participacion

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'desarrollador')
    list_filter = ('genero',)
    search_fields = ('nombre', 'desarrollador')

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'nombre', 'pais', 'activo')
    list_filter = ('activo', 'pais')
    search_fields = ('nombre', 'tag')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'equipo_id', 'rango_actual', 'pais')
    list_filter = ('rango_actual', 'pais')
    search_fields = ('nickname',)

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'juego_id', 'estado', 'premio_total')
    list_filter = ('estado', 'modalidad')
    search_fields = ('nombre',)

@admin.register(Participacion)
class ParticipacionAdmin(admin.ModelAdmin):
    list_display = ('equipo_id', 'torneo_id', 'posicion_final', 'premio_ganado')
    list_filter = ('torneo_id',)