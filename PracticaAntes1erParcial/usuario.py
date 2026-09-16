def usuario0(usuario,contraseña):
    a="jhona"
    b="123"
    if usuario==a and contraseña==b:
        return True
    else:
        return False
def menu_usuario():

    print("----Menu Usuario----")
    print("-------------------------")
    print("1.Registrar Usuario.")
    print("2.Mostrar Usuario.")
    print("--------------------------")
    opcion=int(input("Ingrese una opcion: "))