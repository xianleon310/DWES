from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Juego(models.Model):
    class Genero(models.TextChoices):
        MOBA = 'MOBA', 'MOBA (League of Legends, Dota 2)'
        FPS = 'FPS', 'First Person Shooter'
        BATTLE_ROYALE = 'BR', 'Battle Royale'
        FIGHTING = 'FIG', 'Juegos de Lucha'
        ESTRATEGIA = 'STR', 'Estrategia en Tiempo Real'
    
    nombre = models.CharField(max_length=100, unique=True)
    genero = models.CharField(max_length=4, choices=Genero.choices)
    desarrollador = models.CharField(max_length=100)
    imagen_portada = models.CharField(max_length=255, blank=True, help_text="URL de la imagen")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
    
    def __str__(self):
        return f"{self.nombre} ({self.get_genero_display()})"


class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tag = models.CharField(max_length=10, unique=True, help_text="Ej: FNC, G2, T1")
    logo = models.CharField(max_length=255, blank=True, help_text="URL del logo")
    pais = models.CharField(max_length=50, blank=True)
    jugador_id = models.ForeignKey('Jugador', on_delete=models.SET_NULL, null=True, blank=True, related_name='equipo_liderado', db_column='jugador_id')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
    
    def __str__(self):
        return f"{self.tag} - {self.nombre}"


class Jugador(models.Model):
    class Rango(models.TextChoices):
        BRONCE = 'BRO', 'Bronce'
        PLATA = 'PLT', 'Plata'
        ORO = 'ORO', 'Oro'
        PLATINO = 'PLA', 'Platino'
        DIAMANTE = 'DIA', 'Diamante'
        MAESTRO = 'MAS', 'Maestro'
        GRAN_MAESTRO = 'GM', 'Gran Maestro'
        CHALLENGER = 'CHA', 'Challenger'
    
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    equipo_id = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, related_name='jugadores', db_column='equipo_id')
    nickname = models.CharField(max_length=50, unique=True, verbose_name="Nombre en juego")
    avatar = models.CharField(max_length=255, blank=True, help_text="URL de la imagen")
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=50)
    rango_actual = models.CharField(max_length=3, choices=Rango.choices, default=Rango.BRONCE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-rango_actual', 'nickname']
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
    
    def __str__(self):
        equipo_str = f" ({self.equipo_id.tag})" if self.equipo_id else ""
        return f"{self.nickname}{equipo_str}"


class Torneo(models.Model):
    class Modalidad(models.TextChoices):
        LIGA = 'LIG', 'Liga (Todos contra todos)'
        ELIMINACION = 'ELI', 'Eliminación Directa'
        GRUPOS = 'GRP', 'Fase de Grupos + Playoffs'
    
    class Estado(models.TextChoices):
        INSCRIPCION = 'INS', 'Abierto a inscripciones'
        EN_CURSO = 'CUR', 'En curso'
        FINALIZADO = 'FIN', 'Finalizado'
        CANCELADO = 'CAN', 'Cancelado'
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    juego_id = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='torneos', db_column='juego_id')
    equipos = models.ManyToManyField(Equipo, through='Participacion')
    premio_total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Premio total en USD")
    modalidad = models.CharField(max_length=3, choices=Modalidad.choices)
    max_equipos = models.IntegerField(validators=[MinValueValidator(2)], help_text="Número máximo de equipos participantes")
    estado = models.CharField(max_length=3, choices=Estado.choices, default=Estado.INSCRIPCION)
    ubicacion = models.CharField(max_length=200, help_text="Ciudad o 'Online'")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"
    
    def __str__(self):
        return f"{self.nombre} - {self.juego_id.nombre}"


class Participacion(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column='equipo_id')
    torneo_id = models.ForeignKey(Torneo, on_delete=models.CASCADE, db_column='torneo_id')
    fecha_inscripcion = models.DateField(auto_now_add=True)
    posicion_final = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)], help_text="Posición final en el torneo (1=Campeón)")
    premio_ganado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Premio obtenido en USD")
    puntos_obtenidos = models.IntegerField(default=0, help_text="Puntos de ranking conseguidos")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['equipo_id', 'torneo_id'], name='unique_participacion_equipo_torneo')
        ]
        ordering = ['torneo_id', 'posicion_final']
        verbose_name = "Participación"
        verbose_name_plural = "Participaciones"
    
    def __str__(self):
        posicion = f"#{self.posicion_final}" if self.posicion_final else "En curso"
        return f"{self.equipo_id.tag} en {self.torneo_id.nombre} - {posicion}"