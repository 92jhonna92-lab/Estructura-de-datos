#Ejercicio 2 – Sumatoria: Pedir 5 números al usuario, guardarlos en una lista y calcular la sumatoria usando un for y un acumulador.
numeros=[]
sum=0
for i in range(5):
    a=int(input("Ingrese un numero: "))
    numeros.append(a)
    sum=sum+a
print(numeros)
print(f"La suma es: {sum}")
