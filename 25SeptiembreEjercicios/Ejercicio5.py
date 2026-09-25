#Ejercicio 5 – Agregar datos: Empezar con una lista vacía, pedir 3 números y agregarlos usando append(). Luego mostrar la lista.
lista=[]
for i in range(3):
    a=int(input(f"Ingrese numero {i+1}: "))
    lista.append(a)
print(lista)