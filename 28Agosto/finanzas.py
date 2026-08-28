def descuentos():
    print("Ejercicio 16 Precio con descuento")
    precio=float(input("Ingrese precio del producto: "))
    des=precio*0.15
    total=precio-des
    return f"El precio total aplicando 15% de descuento es: {total}"

def impuesto():
    print("Ejercicio 17 IVA")
    precio=float(input("Ingrese precio del producto: "))
    des=precio*0.13
    return f"El impuesto al IVA es: {des}"