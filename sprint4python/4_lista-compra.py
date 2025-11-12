lista_compra = []

def añadirProducto():
    nombreproducto=input("\n¿Cuál es el nombre del producto?\n")
    nombreproducto=nombreproducto.lower().strip()
    duplicado=False
    for i in range(len(lista_compra)):
        if lista_compra[i]==nombreproducto:
            print('Producto ya encontrado en la lista')
            duplicado=True
            break
    if not duplicado:
        lista_compra.append(nombreproducto)

def eliminarProducto():
    nombreproducto=input("\n¿Cuál es el nombre del producto?\n")
    nombreproducto=nombreproducto.lower().strip()
    duplicado=False
    for i in range(len(lista_compra)):
        if lista_compra[i]==nombreproducto:
            duplicado=True
            break
    if duplicado:
        lista_compra.remove(nombreproducto)

def verLista():
    if len(lista_compra)==0:
        print('No hay productos en la lista')
        return True
    else:
        for i in range(len(lista_compra)):
            print (lista_compra[i])

def vaciarLista():
    while True:
        opcion=input("¿Estás seguro? (s/n)")
        opcion=opcion.strip().lower()
        if (opcion!="s" and opcion!="n"):
            continue
        else:
            if opcion=="s":
                lista_compra.clear()
                break
            elif opcion=="n":
                break

while True:
    opcion=input('1.Añadir producto\n2.Eliminar producto\n3.Ver lista\n4.Vaciar lista\n5.Salir\n')
    opcion=opcion.strip()
    opcion=opcion.lower()
    if opcion=="1" or opcion=="añadir producto":
        añadirProducto()
    if opcion=="2" or opcion=="eliminar producto":
        eliminarProducto()
    if opcion=="3" or opcion=="ver lista":
        verLista()
    if opcion=="4" or opcion=="vaciar lista":
        vaciarLista()
    if opcion=="5" or opcion=="salir":
        print('Has salido')
        break