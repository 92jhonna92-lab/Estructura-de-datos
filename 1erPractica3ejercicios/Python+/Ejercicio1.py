montoC=float(input("Ingrese monto de compra: "))
if montoC<=0:
    print("Monto no valido, revise...")
elif montoC>500:
    descuento=montoC*0.1
    montoTotal=montoC-descuento
    print(f"El descuento es: {descuento}")
    print(f"Monto final de la compra es: {montoTotal}")
else:
    print("No aplica descuento")

