for aula in range(1,4):
    suma=0
    print(f"Aula {aula}")
    for estudiante in range(1,5):
        nota=float(input(f"Ingrese nota estudiante {estudiante} del aula {aula}: "))
        print(f"Estudiante {estudiante} nota: {nota}")
        suma=suma+nota
    promedio=suma/4
    print(f"El promedio del aula {aula} es: {promedio}")
print()