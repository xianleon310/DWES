import random
opciones=["piedra","papel","tijeras","lagarto","spock"]
ganadores={
"piedra":["tijeras","lagarto"],
"papel":["piedra","spock"],
"tijeras":["papel","lagarto"],
"lagarto":["spock","papel"],
"spock":["piedra","tijeras"]
}

def ganador(jugada_usuario,jugada_cpu):
    if jugada_usuario==jugada_cpu:
        return 0
    #Se recorren los arrays dentro del diccionario
    elif jugada_cpu in ganadores[jugada_usuario]:
        return 1
    elif jugada_cpu not in ganadores[jugada_usuario]:
        return -1

def generarbatalla():
    while True:
        try:
            numero=int(input("Escribe un número impar mayor o igual a 1: "))
        except ValueError:
            print('No has escrito un número')
            continue
        if numero%2==0 or numero<1:
            print('Debe ser un número impar mayor o igual a 1')
            continue
        else:
            break
    
    victorias_usuario=0
    victorias_cpu=0
    rondas_para_ganar=numero//2+1
    
    while (numero!=0):
        jugadacpu=random.randint(0,4)
        jugadacpu=opciones[jugadacpu]
        
        while True:
            jugada=input("Que quieres sacar?(piedra/papel/tijeras/lagarto/spock): ").lower()
            if jugada in opciones:
                break
            else:
                print("Opción no válida")
        
        print(f"\nTu jugaste: {jugada}")
        print(f"CPU jugo: {jugadacpu}")
        
        resultado_ronda = ganador(jugada, jugadacpu)
        
        if resultado_ronda == 0:
            print("Empate!")
        elif resultado_ronda == 1:
            print("Ganaste esta ronda!")
            victorias_usuario += 1
        else:
            print("CPU gana esta ronda")
            victorias_cpu += 1
        
        print(f"\nMarcador: Tu {victorias_usuario} - CPU {victorias_cpu}")
        print(f"Rondas restantes: {numero}\n")
        
        if victorias_usuario == rondas_para_ganar:
            print("GANASTE LA PARTIDA!")
            break
        elif victorias_cpu == rondas_para_ganar:
            print("CPU GANO LA PARTIDA")
            break
        
        numero=numero-1
    
    else:
        print("\n=== RESULTADO FINAL ===")
        if victorias_usuario > victorias_cpu:
            print("GANASTE LA PARTIDA!")
        else:
            print("CPU GANO LA PARTIDA")
    
    while True:
        otra_vez = input("\nQuieres jugar otra vez? (s/n): ").lower()
        if otra_vez == 's':
            return True
        elif otra_vez == 'n':
            print("Gracias por jugar!")
            return False
        else:
            print("Respuesta no válida")

while True:
    continuar = generarbatalla