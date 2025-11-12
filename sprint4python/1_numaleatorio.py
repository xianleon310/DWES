import random

def calcularnumero(num1,num2):
    num_aleatorio=random.randint(num1,num2)
    intentos=0
    while True:
        try:
            num_usuario=input("Introduce un número  ")
            num_usuario=int(num_usuario)
        except ValueError:
            print("Error:Debes introducir un número válido")
            continue
        if num_usuario<num_aleatorio:
            print('Demasiado bajo')
            intentos=intentos+1
        elif num_usuario>num_aleatorio:
            print('Demasiado alto')
            intentos=intentos+1
        elif num_usuario==num_aleatorio:
            intentos=intentos+1
            print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
            otravez=0
            while (otravez!="s" and otravez!="n"):
                otravez=input("¿Quieres jugar otra vez (s/n)")
                otravez=otravez.lower()
                if otravez=="s":
                    return True # (*)
                elif otravez=="n":
                    print("¡Gracias por jugar!")
                    return False
                
#Se ejecutará el bucle siempre que se retorne desde el método calcular número "True" (*)
while True:
    print ("El programa pensará un número entre 1 y un máximo que tú elijas. Intenta adivinarlo con la menor cantidad de intentos posible.")
    while True:
        opcion=input("Elige la dificultad (fácil,medio,difícil)").lower()
        if opcion=="facil" or opcion=="facil":
            opcion=1
            break
        elif opcion=="medio":
            opcion=2
            break
        elif opcion=="difícil" or opcion=="dificil":
            opcion=3
            break
        else:
            continue
    if opcion==1:
        calcularnumero(1,50)
    if opcion==2:
        calcularnumero(1,100)
    if opcion==3:
        calcularnumero(1,500)
