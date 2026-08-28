def dolares():
    print("Ejercicio 14 Conversor a dolares")
    cantidad=float(input("Ingrese monto a convertir: "))
    conversion=cantidad*6.96
    return conversion

def temperatura():
    print("Ejercicio 15 Conversor temperatura")
    temp=float(input("Ingrese temperatura a convertir(Cº): "))
    conversion=(temp*1.8)+32
    return f"Fº {conversion}" 