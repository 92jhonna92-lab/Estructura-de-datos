def parOimpar(a):
    print("Ejercicio 5 Par o Impar")
    if a%2==0:
        return True
    else:
        return False

def entero(b):
    print("Ejercicio 6 Numero entero")
    if b>0:
        return True
    else:
        return False

def contraseña():
    print("Ejercicio 9 Validador Contraseña")
    a=input("Ingrese una contraseña: ")
    if len(a)>8:
        return True
    else:
        return False