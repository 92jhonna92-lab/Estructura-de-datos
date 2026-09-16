import admin,usuario
def login():
    while True:
    
        a=input("Ingrese usuario: ")
        b=input("Ingrese contraseña: ")
        if admin.admin0(a,b):
            print("Acceso concedido")
            admin.menu_adminitrador()
        elif usuario.usuario0(a,b):
            usuario.menu_usuario()
        else:
            print("Intente nuevamente")
