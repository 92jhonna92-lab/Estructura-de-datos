##temperaturas
for dia in range(1,5):
    suma=0
    for mediciones in range(1,4):
        temp=float(input(f"Ingrese la temperatura del dia {dia} medicion {mediciones}:  "))
        suma=suma+temp
        promedio=suma/3
    print(f"El promedio de las temperaturas en el dia {dia} es: {promedio}")