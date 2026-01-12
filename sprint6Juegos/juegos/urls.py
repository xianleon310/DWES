from django.urls import path
from .views import (
    JuegoListAPIView, JuegoDetailAPIView, JuegoCreateAPIView,
    EquipoListAPIView, EquipoDetailAPIView, EquipoCreateAPIView,
    TorneoListAPIView, TorneoDetailAPIView, TorneoCreateAPIView
)

urlpatterns = [
    path('api/juegos/', JuegoListAPIView.as_view(), name='juego-list'),
    path('api/juegos/<int:pk>/', JuegoDetailAPIView.as_view(), name='juego-detail'),
    path('api/juegos/crear/', JuegoCreateAPIView.as_view(), name='juego-create'),
    
    path('api/equipos/', EquipoListAPIView.as_view(), name='equipo-list'),
    path('api/equipos/<int:pk>/', EquipoDetailAPIView.as_view(), name='equipo-detail'),
    path('api/equipos/crear/', EquipoCreateAPIView.as_view(), name='equipo-create'),
    
    path('api/torneos/', TorneoListAPIView.as_view(), name='torneo-list'),
    path('api/torneos/<int:pk>/', TorneoDetailAPIView.as_view(), name='torneo-detail'),
    path('api/torneos/crear/', TorneoCreateAPIView.as_view(), name='torneo-create'),
]