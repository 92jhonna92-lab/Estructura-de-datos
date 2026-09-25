#Ejercicio 4 – Contar elementos: Crear una lista de 6 números y usar len() para mostrar cuántos elementos tiene.
numeros=[]
for i in range(6):
    a=int(input(f"Ingrese numero {i+1}: "))
    numeros.append(a)
print(numeros)
print(f"Tiene {len(numeros)} elementos")