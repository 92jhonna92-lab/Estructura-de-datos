for aula in range(1,5):
    presentes=0
    faltas=0
    print(f"Aula {aula}")
    for estudiante in range(1,7):
        while True:

            asis=input(f"Ingrese asistencia del estudiante {estudiante} del aula {aula}(1=presente - 0=falta ): ")
            if(asis=="1"):
                presentes=presentes+1
                break
            elif(asis=="0"):
                faltas=faltas+1
                break
            else:
                print("Caracter no valido, Ingrese 1 si asistio, 0 si falto")

    print(f"Las asistencia del aula {aula} es: {presentes}")
    print(f"Las faltas del aula {aula} es: {faltas}")

print()