#Ejercicio 3 – Promedio: Pedir 4 notas, guardarlas en una lista y mostrar la sumatoria y el promedio.
notas=[]
sum=0
prom=0

for i in range(4):
    a=int(input(f"ingrese nota {i+1}: "))
    notas.append(a)
    sum=sum+a
prom=sum/len(notas)
print(notas)
print("La sumatoria es: ",sum)
print("El promedio es: ", prom)