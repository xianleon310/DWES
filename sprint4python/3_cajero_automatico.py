cuenta = {"nombre": "Ana", "saldo": 1200.0}
def consultarSaldo():
    for clave,valor in cuenta.items():
        if clave=="nombre":
            print(f"{clave}:{valor}")
        elif clave=="saldo":
            print(f"{clave}:{valor:.2f}")

def ingresarDinero():
    while True:
        try:
            cantidad=float(input("¿Qué cantidad?"))
        except ValueError:
            continue
        if (cantidad>=0):
            cuenta["saldo"]=cuenta["saldo"]+cantidad
            break
        else:
            continue


def retirarDinero():
    while True:
        try:
            cantidad=float(input("¿Qué cantidad?"))
        except ValueError:
            continue
        if cantidad>cuenta["saldo"]:
            print('Saldo insuficiente')
            break
        elif cantidad<=cuenta["saldo"]:
            cuenta["saldo"]=cuenta["saldo"]-cantidad
            break


while True:
    opcion=input('1.Consultar saldo\n2.Ingresar dinero\n3.Retirar dinero\n4.Salir\n')
    opcion=opcion.strip()
    opcion=opcion.lower()
    if opcion=="1" or opcion=="consultar saldo":
        consultarSaldo()
    if opcion=="2" or opcion=="ingresar dinero":
        ingresarDinero()
    if opcion=="3" or opcion=="retirar dinero":
        retirarDinero()
    if opcion=="4" or opcion=="salir":
        print('\nHas salido del programa')
        break
