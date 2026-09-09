def div():
    try:
        a=int(input("Ingrese un numero: "))
        b=int(input("Ingrese otro numero "))
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except ValueError:
        print("Valor no valido")