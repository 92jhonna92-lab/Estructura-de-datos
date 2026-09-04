import usuario

def admin0(usuario,contraseña):
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
                print("-----Registrar nuevo usuario----")
                User=input("Ingrese usuario: ")
                Pass=input("Ingrese contraseña: ")
                registrado=usuario.registrar_usuario(User,Pass)
                if registrado:
                    print("Usuario registrado correctamente")
                else:
                    print("El usuario ya existe")
                break
            case 2:
                usuario.ver_usuario()

            case _:
                print("Opcion no valida")
                break