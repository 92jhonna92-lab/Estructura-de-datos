def admin(usuario,contraseña):
    a="admin"
    b="admin"
    if usuario==a and contraseña==b:
        return True
    else:
        return False
    
def menu_adminitrador():
    print("----Menu Adminitrador----")
    print("-------------------------")
    print("1.Registrar Usuario.")
    print("2.Mostrar Usuario.")
    print("3.Buscar Usuario.")
    print("4.Modificar Usuario.")
    print("5.Eliminar Usuario.")
    print("5.Cerrar sesion.")
    print("--------------------------")
    opcion=int(input("Ingrese una opcion: "))
    while True:
        match opcion:
            case 1:
                print("en desarrollo")
                break
            case _:
                print("Opcion no valida")
                break