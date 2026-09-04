import administrador,funciones,usuario

print("-----Login------")
us=input("Ingrese usuario: ")
password=input("Ingrese contraseña: ")
while True:
    if administrador.admin0(us,password):
        print("--Acceso concedido--")
        administrador.menu_adminitrador()
    else:
        print("--Acceso denegado--")
        break

