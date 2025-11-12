from Tareas import Tarea
tareas = []
def crearTarea():
    titulo=input("Introduce un título\n").strip().lower()
    descripcion=input("Introduce una descripcion\n").strip().lower()
    nueva_tarea=Tarea(titulo,descripcion)
    tareas.append(nueva_tarea)

def mostrarTareas():
    if len(tareas) == 0:  
        print("No hay tareas en la lista\n")
    else:
        for i in range(len(tareas)):
            print (tareas[i].mostrar_info())

def marcarTarea():
    titulo=input("Introduce el titulo").strip().lower()
    for i in range(len(tareas)):
        if titulo==tareas[i].titulo:
            tareas[i].marcar_completada()
            break

def editarTarea():
    tituloviejo=input("Qué título quieres modificar?").strip().lower()
    for i in range (len(tareas)):
        if tareas[i].titulo==tituloviejo:
            titulo=input("Introduce un nuevo título\n").strip().lower()
            descripcion=input("Introduce una nueva descripcion\n").strip().lower()
            tareas[i].editar(titulo,descripcion)
            break

def eliminarTarea():
    tituloviejo=input("Qué título quieres modificar?").strip().lower()
    for i in range (len(tareas)):
        if tareas[i].titulo==tituloviejo:
            tareas.pop(i)
            break



while True:
    opcion=input('\n\n1.Crear tareas\n2.Mostrar todas\n3.Marcar como completada\n4.Editar tarea\n5.Eliminar tarea\n6.Salir\n')
    opcion=opcion.strip()
    opcion=opcion.lower()
    if opcion=="1" or opcion=="crear tarea":
        crearTarea()
    if opcion=="2" or opcion=="mostrar todas":
        mostrarTareas()
    if opcion=="3" or opcion=="marcar como completada":
        marcarTarea()
    if opcion=="4" or opcion=="editar tarea":
        editarTarea()
    if opcion=="5" or opcion=="eliminar tarea":
        eliminarTarea()
    if opcion=="6" or opcion=="salir":
        print('Has salido')
        break