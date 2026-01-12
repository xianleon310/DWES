from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Juego, Equipo, Torneo
from .serializers import JuegoSerializer, EquipoSerializer, TorneoSerializer

class JuegoListAPIView(APIView):
    def get(self, request):
        juegos = Juego.objects.all()
        serializer = JuegoSerializer(juegos, many=True)
        return Response(serializer.data)

class JuegoDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            juego = Juego.objects.get(pk=pk)
            serializer = JuegoSerializer(juego)
            return Response(serializer.data)
        except Juego.DoesNotExist:
            return Response({'error': 'Juego no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class JuegoCreateAPIView(APIView):
    def post(self, request):
        serializer = JuegoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipoListAPIView(APIView):
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)

class EquipoDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            equipo = Equipo.objects.get(pk=pk)
            serializer = EquipoSerializer(equipo)
            return Response(serializer.data)
        except Equipo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class EquipoCreateAPIView(APIView):
    def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TorneoListAPIView(APIView):
    def get(self, request):
        torneos = Torneo.objects.all()
        serializer = TorneoSerializer(torneos, many=True)
        return Response(serializer.data)

class TorneoDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            torneo = Torneo.objects.get(pk=pk)
            serializer = TorneoSerializer(torneo)
            return Response(serializer.data)
        except Torneo.DoesNotExist:
            return Response({'error': 'Torneo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class TorneoCreateAPIView(APIView):
    def post(self, request):
        serializer = TorneoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)