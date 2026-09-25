#Ejercicio 6 – Mini reto: Pedir 5 edades, guardarlas en una lista y calcular el promedio de las edades.
edades=[]
sum=0
prom=0

for i in range(5):
    a=int(input(f"ingrese edad {i+1}: "))
    edades.append(a)
    sum=sum+a
prom=sum/len(edades)
print(edades)
print("La sumatoria de edades es: ",sum)
print("El promedio de edades es: ", prom)