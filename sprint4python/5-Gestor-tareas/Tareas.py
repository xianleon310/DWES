class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
    
    def mostrar_info(self):
        if self.completada:
            estado="Completada"
        else:
            estado="Pendiente"
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {estado}"
    
    def marcar_completada(self):
        self.completada = True
    
    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion