##Una universidad tiene 4 aulas, y cada aula tiene 6 estudiantes.
##Recorrer las 4 aulas.
##Dentro de cada aula, recorrer los 6 estudiantes.
##Contar cuántos presentes y faltas hay en cada aula.
##Al terminar cada aula, mostrar sus resultados.
##Si el número introducido no es 1 ni 0, mostrar "Carácter no válido" y volver a pedir la asistencia del mismo estudiante.}
for aula in range(1,5):
    conts=0
    contn=0
    print(f"Asistencia Aula {aula}")
    for estudiante in range(1,7):
        while True:
            asist=int(input(f"El estudiante {estudiante} Asistio? 1(si)- 0(no): "))
            if asist==1:
                conts=conts+1
                break
            elif asist==0:
                contn=contn+1
                break
            else:
                print("Caracter no valido, intente nuevamente")
                
    print(f"En la aula {aula} hay {conts} que asistieron")
    print(f"En la aula {aula} hay {contn} que no asistieron")
