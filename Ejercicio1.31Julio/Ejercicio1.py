##Practica de match
tipo_vehiculo=input("Ingrese tipo de vehiculo: ")
Tipo=tipo_vehiculo.lower()

match Tipo:
    case "auto":
        tarifa=2
    case "moto":
        tarifa=3
    case "camion":
        tarifa=5
    case _:
        print("Opcion no valida")
        exit()

hora=int(input("Ingrese hora del dia(1-24): "))
if (hora>6 and hora<=9) or (hora>17 and hora<22):
    incremento=tarifa*1.15

    print(f"La tarifa es {incremento}")
else:
    print("No es hora pico, no hay incremento")
