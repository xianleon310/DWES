from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tjuegos
# Create your views here.
def pagina_de_prueba(request):
    return HttpResponse("<h1>Hola caracola</h1>")

def devolver_canciones(request):
    lista= Tjuegos.objects.all()
    respuesta_final=[]
    for fila_sql in lista:
        diccionario={}
        diccionario['id']=fila_sql.id
        diccionario['nombre']=fila_sql.nombre
        diccionario['descripcion']=fila_sql.descripcion
        diccionario['plataforma']=fila_sql.plataforma
        respuesta_final.append(diccionario)
    return JsonResponse(respuesta_final,safe=False)
