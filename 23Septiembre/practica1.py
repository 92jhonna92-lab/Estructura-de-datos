productos=[]
for i in range(5):
    nombre=input("Ingrese producto: ").strip()
    productos.append(nombre)
    productos.sort()
    for producto in productos:
        print(f"- {producto}")

print("---Busqueda: ---")
x=input("Ingrese producto a buscar: ").strip()
if x in productos:
    print(f"El producto {x} si esta en la lista")
else:
    print(f"El producto {x} no esta en la lista")

