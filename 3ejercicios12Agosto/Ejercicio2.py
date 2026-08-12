for categoria in range(1,4):
    suma=0
    print(f"Categoria {categoria}")
    for producto in range(1,5):
        precio=float(input(f"Ingrese precio producto {producto} de la categoria {categoria}: "))
        print(f"Precio producto {producto}")
        suma=suma+precio
    print(f"Total de ventas de la categoria {categoria} = {suma}")
print()