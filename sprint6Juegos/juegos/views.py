from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Count, Sum
from .models import Juego, Equipo, Torneo, Jugador, Participacion
from .serializers import (
    JuegoSerializer, EquipoSerializer, TorneoSerializer,
    JugadorSerializer, ParticipacionSerializer,
    InscribirEquipoSerializer, FinalizarTorneoSerializer,
    CambiarEstadoTorneoSerializer, AsignarCapitanSerializer
)
from .filters import TorneoFilter, EquipoFilter, JugadorFilter

#MODELVIEWSET:
#crea automáticamente la opcion de:
# GET /api/juegos | GET /api/juegos/5 | POST /api/juegos | PUT /api/juegos/5 | PATCH /api/juegos/5 | DELETE /api/juegos/5
class JuegoViewSet(ModelViewSet):
    #Una vez implementado el viewset y teniendo las consultas,
    # obtiene todos los juegos de la base de datos
    queryset = Juego.objects.all()
    #llama al método JuegoSerializer, el cual se encarga de pasar
    #los campos del model a formato json
    serializer_class = JuegoSerializer
    
    #Añade capacidades a dichas consultas, como el buscar y ordenar, que se definen abajo
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #permite: /api/juegos/?genero=MOBA , comparando lo que ponga el usuario con el campo genero del models
    filterset_fields = ['genero']
    #permite: /api/juegos/?search=League, comparando lo que ponga el usuario con el campo nombre o desarrollador del models
    search_fields = ['nombre', 'desarrollador']
    #permite: /api/juegos/?ordering=-created_at  -> mas recientes primero
    ordering_fields = ['nombre', 'created_at']
    #ordenamiento por defecto si no se especifica
    ordering = ['nombre']


class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EquipoFilter
    search_fields = ['nombre', 'tag', 'pais']
    ordering_fields = ['nombre', 'created_at', 'activo']
    ordering = ['-created_at']

    #Se aplica un post específico -> /api/equipos/5/asignar_capitan
    #siendo detail=True se tiene que especificar la primary key, en caso contrario no
    #por ejemplo, si detail fuera 'detail=False' la peticion post sería
    #-> /api/equipos/asignar_capitan
    @action(detail=True, methods=['post'])
    def asignar_capitan(self, request, pk=None):
        
        #guarda en la variable equipo el objeto obtenido en el que coinciden
        #la pk del método con la pk de equipo:
        #EJEMPLO:
        #POST /api/equipos/5/asignar_capitan -> pk=5
        #equipo=self.get_object -> SELECT * FROM equipos WHERE id=5
        equipo = self.get_object()
        
        #request.data contiene lo que el usuario mandó a través del POST
        #y llama al método AsignarCapitanSerializer para deshacer el json 
        # y convertirlo a python
        serializer = AsignarCapitanSerializer(data=request.data)
        #si no es válido retorna error e internamente convierte de String a int 
        #(en este caso)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #serializer.validated_data={'jugador_id':10}

        #se guarda en la variable jugador_id el id (en este caso el 10)
        jugador_id = serializer.validated_data['jugador_id']
        
        #se intenta obtener el jugador que coincida con el id del obtenido 
        #en la anterior linea
        try:
            jugador = Jugador.objects.get(id=jugador_id)
        #en caso contrario retorna un error, ya que no se ha encontrado
        except Jugador.DoesNotExist:
            return Response(
                {"error": "Jugador no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        #Si el equipo_id perteneciente a Jugador no coincide con la pk de Equipo
        #significa que no pertenece al equipo, por lo cual retornará error
        if jugador.equipo_id != equipo:
            return Response(
                {"error": "El jugador no pertenece a este equipo"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        #En caso contrario se guardarán los siguientes datos como respuesta de que está 
        # todo correcto
        capitan_anterior = equipo.jugador_id
        equipo.jugador_id = jugador
        equipo.save()
        
        return Response(
            {
                "mensaje": "Capitán asignado correctamente",
                "capitan_anterior": capitan_anterior.nickname if capitan_anterior else None,
                "nuevo_capitan": jugador.nickname
            },
            status=status.HTTP_200_OK
        )
    

    #Se crea un GET /api/equipos/activos
    @action(detail=False, methods=['get'])
    def activos(self, request):
        #guarda en el objeto "equipos_activos" todos los equipos que tienen el campo 
        # activo a true
        equipos_activos = Equipo.objects.filter(activo=True)
        #
        serializer = self.get_serializer(equipos_activos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def estadisticas(self, request, pk=None):
        equipo = self.get_object()
        
        participaciones = Participacion.objects.filter(equipo_id=equipo)
        
        stats = {
            "nombre": equipo.nombre,
            "tag": equipo.tag,
            "total_torneos": participaciones.count(),
            "torneos_ganados": participaciones.filter(posicion_final=1).count(),
            "podios": participaciones.filter(posicion_final__lte=3, posicion_final__isnull=False).count(),
            "premios_totales": participaciones.aggregate(total=Sum('premio_ganado'))['total'] or 0,
            "jugadores_actuales": equipo.jugadores.count()
        }
        
        return Response(stats, status=status.HTTP_200_OK)


class TorneoViewSet(ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TorneoFilter
    search_fields = ['nombre', 'descripcion', 'ubicacion']
    ordering_fields = ['nombre', 'premio_total', 'created_at', 'max_equipos']
    ordering = ['-created_at']

    @action(detail=True, methods=['post'])
    def inscribir_equipo(self, request, pk=None):
        torneo = self.get_object()
        
        serializer = InscribirEquipoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        equipo_id = serializer.validated_data['equipo_id']
        
        try:
            equipo = Equipo.objects.get(id=equipo_id)
        except Equipo.DoesNotExist:
            return Response(
                {"error": "Equipo no encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if torneo.estado != 'INS':
            return Response(
                {"error": "El torneo no está en fase de inscripción"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        participaciones_actuales = torneo.participaciones.count()
        if participaciones_actuales >= torneo.max_equipos:
            return Response(
                {"error": "Torneo completo"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        participacion, creada = Participacion.objects.get_or_create(
            torneo_id=torneo,
            equipo_id=equipo
        )
        
        if not creada:
            return Response(
                {"error": "El equipo ya está inscrito en este torneo"},
                status=status.HTTP_409_CONFLICT
            )
        
        return Response(
            {
                "mensaje": "Equipo inscrito correctamente",
                "torneo": torneo.nombre,
                "equipo": equipo.nombre,
                "participaciones_actuales": participaciones_actuales + 1,
                "max_equipos": torneo.max_equipos
            },
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def cambiar_estado(self, request, pk=None):
        torneo = self.get_object()
        
        serializer = CambiarEstadoTorneoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        nuevo_estado = serializer.validated_data['nuevo_estado']
        estado_anterior = torneo.estado
        
        if estado_anterior == nuevo_estado:
            return Response(
                {"error": "El torneo ya está en ese estado"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        torneo.estado = nuevo_estado
        torneo.save()
        
        return Response(
            {
                "mensaje": "Estado cambiado correctamente",
                "estado_anterior": estado_anterior,
                "estado_actual": nuevo_estado
            },
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def finalizar(self, request, pk=None):
        torneo = self.get_object()
        
        if torneo.estado == 'FIN':
            return Response(
                {"error": "El torneo ya está finalizado"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = FinalizarTorneoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        posiciones = serializer.validated_data['posiciones']
        
        for pos_data in posiciones:
            participacion_id = pos_data.get('participacion_id')
            posicion_final = pos_data.get('posicion_final')
            premio_ganado = pos_data.get('premio_ganado', 0)
            
            try:
                participacion = Participacion.objects.get(
                    id=participacion_id,
                    torneo_id=torneo
                )
                participacion.posicion_final = posicion_final
                participacion.premio_ganado = premio_ganado
                participacion.save()
            except Participacion.DoesNotExist:
                return Response(
                    {"error": f"Participación {participacion_id} no encontrada"},
                    status=status.HTTP_404_NOT_FOUND
                )
        
        torneo.estado = 'FIN'
        torneo.save()
        
        return Response(
            {
                "mensaje": "Torneo finalizado correctamente",
                "participaciones_actualizadas": len(posiciones)
            },
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        estadisticas = {
            "total_torneos": Torneo.objects.count(),
            "torneos_activos": Torneo.objects.filter(estado='CUR').count(),
            "torneos_inscripcion": Torneo.objects.filter(estado='INS').count(),
            "torneos_finalizados": Torneo.objects.filter(estado='FIN').count(),
            "premio_total_distribuido": Torneo.objects.filter(estado='FIN').aggregate(
                total=Sum('premio_total')
            )['total'] or 0,
            "por_juego": list(
                Torneo.objects.values('juego_id__nombre')
                .annotate(cantidad=Count('id'))
            )
        }
        
        return Response(estadisticas, status=status.HTTP_200_OK)


class JugadorViewSet(ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = JugadorFilter
    search_fields = ['nickname', 'pais']
    ordering_fields = ['nickname', 'rango_actual', 'created_at']
    ordering = ['-rango_actual', 'nickname']

    @action(detail=False, methods=['get'])
    def sin_equipo(self, request):
        jugadores_libres = Jugador.objects.filter(equipo_id__isnull=True)
        serializer = self.get_serializer(jugadores_libres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def por_rango(self, request):
        rango = request.query_params.get('rango', 'CHA')
        
        if rango not in dict(Jugador.Rango.choices):
            return Response(
                {"error": "Rango no válido"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        jugadores = Jugador.objects.filter(rango_actual=rango)
        serializer = self.get_serializer(jugadores, many=True)
        
        return Response(
            {
                "rango": rango,
                "total": jugadores.count(),
                "jugadores": serializer.data
            },
            status=status.HTTP_200_OK
        ) 


class ParticipacionViewSet(ModelViewSet):
    queryset = Participacion.objects.all()
    serializer_class = ParticipacionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['equipo_id', 'torneo_id', 'posicion_final']
    ordering_fields = ['posicion_final', 'premio_ganado', 'fecha_inscripcion']
    ordering = ['posicion_final']