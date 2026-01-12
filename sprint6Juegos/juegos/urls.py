from django.urls import path
from .views import JuegoListAPIView, JuegoDetailAPIView, JuegoCreateAPIView

urlpatterns = [
    path('api/juegos/', JuegoListAPIView.as_view(), name='juego-list'),
    path('api/juegos/<int:pk>/', JuegoDetailAPIView.as_view(), name='juego-detail'),
    path('api/juegos/crear/', JuegoCreateAPIView.as_view(), name='juego-create'),
]