def admin0(usuario,contraseña):
    a="admin"
    b="admin"
    if usuario==a and contraseña==b:
        return True
    else:
        return False

def menu_adminitrador():
    while True:
        try:
            print("----Menu Adminitrador----")
            print("-------------------------")
            print("1.Registrar Usuario.")
            print("2.Mostrar Usuario.")
            print("3.Buscar Usuario.")
            print("4.Modificar Usuario.")
            print("5.Eliminar Usuario.")
            print("6.Cerrar sesion.")
            print("--------------------------")
            opcion=int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    print("-----Registrar nuevo usuario----")
                    User=input("Ingrese usuario: ")
                    Pass=input("Ingrese contraseña: ")

                case 2:
                    print("----Listado de usuarios---- ")

                case 3:
                    print("----Buscar Usuario----")
                    
                case 4:
                    print("----Modificar Usuario----")

                case 5:
                    print("----Eliminar Usuario----")
                case 6:
                    print("Saliendo")
                    return
                case _:
                    print("Opcion no valida")
        except ValueError:
            print("Valor no valido")