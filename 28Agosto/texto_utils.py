def nombre():
    print("Ejercicio 10 Nombre Completo")
    a= input("Ingresa tu nombre: ")
    b= input("Ingresa tu apellido: ")
    a=a.upper()
    b=b.upper()
    c=a+b
    return c

def primeraLetra():
    print("Ejercicio 12 Primera Letra")
    a=input("Ingresa una palabra: ")
    primera_letra=a[0]
    primera_letra=primera_letra.upper()
    return primera_letra

def total_caracteres():
    print("Ejercicio 11 Total Caracteres")
    palabra=input("Ingrese una palabra o frase: ")
    cantidad= len(palabra)
    return cantidad

def letraA():
    print("Ejercicio 13 Empieza con A?")
    palabra=input("Ingrese una palabra: ")
    primera_letra=palabra[0]
    primera_letra=primera_letra.upper()
    if primera_letra=="A":
        return True
    else:
        return False