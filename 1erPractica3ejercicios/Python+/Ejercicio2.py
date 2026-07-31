##Ejercicio2
cliente=input("Ingrese tipo de cliente(A,B,C): ")
cliente=cliente.upper()
if cliente=="A" or cliente=="B" or cliente=="C":
    if cliente=="A":
        MontoTotal=float(input("Ingrese monto total: "))
        if MontoTotal>1000:
            descuento=MontoTotal*0.2
            print(f"El descuento es: {descuento}")
        else:
            descuento=MontoTotal*0.15
            print(f"El descuento es: {descuento}")
    elif cliente=="B":
            MontoTotal=float(input("Ingrese monto total: "))
            if MontoTotal>1000:
                descuento=MontoTotal*0.1
                print(f"El descuento es: {descuento}")
            else:
                descuento=MontoTotal*0.05
                print(f"El descuento es: {descuento}")
    if cliente=="C":
         print("No recibe ningun descuento...")
else:
     print("Opcion no valida")