print("1.-Niño, 2.- Adulto, 3.- Adulto Mayor")
tipo_entrada=input("Ingrese tipo de entrada(1,2,3): ")

match tipo_entrada:
    case "1":
        a="Niño"
        tarifa=20
    case "2":
        a="Adulto"
        tarifa=40
    case "3":
        a="Adulto mayor"
        tarifa=25
    case _:
        print("Opcion no valida")
        exit()

dia=input("Ingrese dia de la semana: ")
match dia:
    case "Lunes":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")
    case "Martes":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")

    case "Miercoles":
        descu=tarifa*0.20
        Total=tarifa-descu
        print(f"Tipo de entrada: {a}---Descuento: {descu}---Total a pagar: {Total}")
    case "Jueves":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")
    case "Viernes":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")
    case "Sabado":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")
    case "Domingo":
        print(f"Tipo de entrada: {a}---No aplica descuento---Total a pagar: {tarifa}")
    case _:
        print("Opcion no valida")
        exit()
