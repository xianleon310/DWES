from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Juego

class JuegoListAPIView(APIView):
    """GET: Listar todos los juegos"""
    def get(self, request):
        juegos = Juego.objects.all()
        
        data = []
        for juego in juegos:
            data.append({
                'id': juego.id,
                'nombre': juego.nombre,
                'genero': juego.genero,
                'desarrollador': juego.desarrollador
            })
        
        return Response(data)

class JuegoDetailAPIView(APIView):
    """GET: Obtener un juego por id"""
    def get(self, request, pk):
        try:
            juego = Juego.objects.get(pk=pk)
            data = {
                'id': juego.id,
                'nombre': juego.nombre,
                'genero': juego.genero,
                'desarrollador': juego.desarrollador,
                'imagen_portada': juego.imagen_portada
            }
            return Response(data)
        except Juego.DoesNotExist:
            return Response({'error': 'Juego no encontrado'}, status=404)

class JuegoCreateAPIView(APIView):
    """POST: Crear un nuevo juego"""
    def post(self, request):
        data = request.data
        
        # Validación manual básica
        if not data.get('nombre') or not data.get('genero'):
            return Response({'error': 'Nombre y género son obligatorios'}, status=400)
        
        juego = Juego.objects.create(
            nombre=data.get('nombre'),
            genero=data.get('genero'),
            desarrollador=data.get('desarrollador', '')
        )
        
        return Response({
            'id': juego.id,
            'nombre': juego.nombre,
            'genero': juego.genero,
            'desarrollador': juego.desarrollador
        }, status=201)