##Una profesora tiene 3 estudiantes y cada estudiante tiene 4 notas:
## 1 use un for dentro de otro for
## 2 pida las notas de cada estudiante
## 3 calcule el promedio de cada estudiante
## 4 indique el estudiante aprobo o no (>=60)

for estudiante in range(1,4):
    notaT=0
    for notas in range(1,5):
        nota=int(input(f"ingrese del estudiante {estudiante} la nota {notas}: "))
        notaT=notaT+nota
    promedio=notaT/4
    print(f"El promedio es: {promedio}")
    if promedio>=60:
        print("El estudiante aprobo")
    else:
        print("El estudiante reprobo")