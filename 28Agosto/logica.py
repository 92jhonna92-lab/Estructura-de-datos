
def mayor():
    print("Ejercicio 7 Numero Mayor")
    c=int(input("Ingrese un primer numero: "))
    d=int(input("Ingrese un segundo numero: "))
    e=int(input("Ingrese un tercer numero: "))
    if (c>d) and (c>e):
        return f"El mayor es: {c}"
    elif (d>c) and (d>e):
        return f"El mayor es: {d}"
    elif (e>c) and (e>d):
        return f"El mayor es: {e}"

def evaluador():
    print("Ejercicio 8 Evualador")
    a=int(input("Ingrese una nota(0-100): "))
    if a>=51:
        return "Aprobado"
    else:
        return "Reprobado"

