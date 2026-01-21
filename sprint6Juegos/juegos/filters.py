import django_filters
from .models import Torneo, Equipo, Jugador

class TorneoFilter(django_filters.FilterSet):
    premio_min = django_filters.NumberFilter(
        field_name="premio_total",
        lookup_expr="gte",
        label="Premio mínimo"
    )
    premio_max = django_filters.NumberFilter(
        field_name="premio_total",
        lookup_expr="lte",
        label="Premio máximo"
    )
    equipos_min = django_filters.NumberFilter(
        field_name="max_equipos",
        lookup_expr="gte"
    )
    equipos_max = django_filters.NumberFilter(
        field_name="max_equipos",
        lookup_expr="lte"
    )
    nombre_contiene = django_filters.CharFilter(
        field_name="nombre",
        lookup_expr="icontains",
        label="Nombre contiene"
    )
    
    class Meta:
        model = Torneo
        fields = {
            'estado': ['exact'],
            'modalidad': ['exact'],
            'juego_id': ['exact'],
        }


class EquipoFilter(django_filters.FilterSet):
    pais_contiene = django_filters.CharFilter(
        field_name="pais",
        lookup_expr="icontains"
    )
    
    class Meta:
        model = Equipo
        fields = {
            'activo': ['exact'],
            'pais': ['exact', 'icontains'],
        }


class JugadorFilter(django_filters.FilterSet):
    rango_minimo = django_filters.ChoiceFilter(
        field_name="rango_actual",
        lookup_expr="gte",
        choices=Jugador.Rango.choices
    )
    
    class Meta:
        model = Jugador
        fields = {
            'rango_actual': ['exact'],
            'pais': ['exact', 'icontains'],
            'equipo_id': ['exact', 'isnull'],
        }