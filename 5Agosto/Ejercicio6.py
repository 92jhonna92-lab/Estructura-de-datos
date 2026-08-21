##Produccion 35

for maquinas in range (1,4):
    total=0
    for productos in range(1,6):
        fabricados=int(input(f"Ingrese productos fabricados en el dia {productos} de la maquina {maquinas}: "))
        total=total+fabricados
    print(f"El total de productos fabricados por la maquina {maquinas} hasta el dia {productos} es: {total}")
