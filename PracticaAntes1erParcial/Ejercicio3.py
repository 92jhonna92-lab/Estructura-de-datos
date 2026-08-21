##Hay 3 equipos. Cada equipo tiene 4 jugadores.
##Para cada jugador debes pedir:
##Edad
##Cantidad de puntos obtenidos
##El programa debe:
##Recorrer los 3 equipos.
##Recorrer los 4 jugadores de cada equipo.
##Si la edad es menor de 18, mostrar: "Jugador menor de edad"
##Si tiene 50 puntos o más, mostrar: "Buen rendimiento"
##Si tiene menos de 50 puntos, mostrar: "Rendimiento bajo"
##Calcular el total de puntos de cada equipo.
##Calcular el promedio de puntos de cada equipo.
##Al final, indicar cuál de los 3 equipos obtuvo mayor cantidad de puntos.}
mayor=0
equipo_mayor=0
for equipo in range(1,4):
    totalpe=0
    totalpj=0
    promedio=0
    
    for jugadores in range(1,5):
        edad=int(input(f"Ingrese edad del jugador {jugadores} del equipo {equipo}: "))    
        if edad<18:
            print("Jugador menor de edad")
        puntos=int(input(f"Ingrese cantidad de puntos obtenidos del jugador {jugadores}: "))
        if puntos>=50:
            print("Buen rendimiento")
        elif puntos<=50:
            print("Rendimiento bajo")
        totalpj=totalpj+puntos
        promedio=totalpj/4
    if totalpj>mayor:
        mayor=totalpj
        equipo_mayor=equipo
    totalpe=totalpe+totalpj

    print(f"La suma de puntos del equipo {equipo} es {totalpe}") 
    print(f"el promedio del equipo {equipo} es: {promedio}")
    print(f"El equipo {equipo_mayor} tiene el mayor numero de puntos {mayor}")

