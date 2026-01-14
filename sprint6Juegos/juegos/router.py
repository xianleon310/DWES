from rest_framework.routers import DefaultRouter
from .views import JuegoViewSet, EquipoViewSet, TorneoViewSet

router = DefaultRouter()
router.register(r'juegos', JuegoViewSet, basename='juego')
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'torneos', TorneoViewSet, basename='torneo')