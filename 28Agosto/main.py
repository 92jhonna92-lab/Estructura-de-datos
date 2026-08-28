import ejercicios,operaciones,geometria,validador,logica,texto_utils,conversor,finanzas,tiempo,auth
while True:
    print("---MENU DE EJERCICIOS---")
    op=int(input("Ingrese numero de ejercicio: "))
    match op:
        case 1:
            print(ejercicios.resta(10,10))
        case 2:
            print(operaciones.multiplicacion(10,10))
        case 3:
            print(geometria.radio(10))
        case 4:
            print(geometria.area_triangulo(5,4))
        case 5:
            a=int(input("Ingrese un numero(Par o impar): "))
            print(validador.parOimpar(a))
        case 6:
            b=int(input("Ingrese un numero(<0=false): "))
            print(validador.entero(b))
        case 7:
            m=logica.mayor()
            print(m)
        case 8:
            print(logica.evaluador())
        case 9:
            print(validador.contraseña())
        case 10:
            print(texto_utils.nombre())
        case 11:
            print(texto_utils.total_caracteres())
        case 12:
            print(texto_utils.primeraLetra())
        case 13:
            print(texto_utils.letraA())
        case 14:
            print(conversor.dolares())
        case 15:
            print(conversor.temperatura())
        case 16:
            print(finanzas.descuentos())
        case 17:
            print(finanzas.impuesto())
        case 18:
            print(tiempo.tiemp())
        case 19:
            if auth.login()==True:
                print("Acceso concedidio")
            else:
                print("Acceso denegado")
        case _:
            print("NO valido")
            break


