def login():
    print("Ejercicio 19 LOGIN")
    usuario=input("Ingrese usuario: ")
    contra=input("Ingrese contraseña: ")
    if usuario=="admin" and contra=="1234":
        return True
    else:
        return False