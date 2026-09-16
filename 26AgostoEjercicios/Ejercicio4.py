edad=int(input("Ingrese la edad: "))
def verificacion():
    if edad<=18:
        print(True)
    else:
        print(False)
verificacion()

edi=int(input("Ingresala"))
def verificacion2(edad):
    if edad<=18:
        return True
    else:
        return False
print(verificacion2(edi))