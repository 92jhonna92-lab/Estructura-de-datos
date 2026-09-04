Usuarios=[]
def registrar_usuario(usuario,contraseña):
    for u in Usuarios:
        if u["usuario"]==usuario:
            return False
    if len(Usuarios)==0:
        nuevo_id=1
    else:
        nuevo_id=max(u["id"] for u in Usuarios)+1

    nuevo_usuario={
        "id":nuevo_id,
        "usuario":usuario,
        "contraseña":contraseña
    }
    Usuarios.append(nuevo_usuario)
    return True

def ver_usuario():

    return Usuarios

def eliminar_usuario():
    Usuarios=()

