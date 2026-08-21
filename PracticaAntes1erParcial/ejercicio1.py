##Una profesora tiene 3 estudiantes y cada estudiante tiene 4 notas:
## 1 use un for dentro de otro for
## 2 pida las notas de cada estudiante
## 3 calcule el promedio de cada estudiante
## 4 indique el estudiante aprobo o no (>=60)

for estudiante in range(1,4):
    print(f"Ingrese notas estudiante {estudiante}: ")
    total=0
    for nota in range(1,5):
        notas=float(input(f"Ingrese nota {nota} del estudiante {estudiante}: "))
        total=total+notas
    promedio=total/4
    if promedio>=60:
        print(f"Estudiante aprobado, Promedio de: {promedio}")
    else:
        print(f"Estudiante reprobado, Promedio de: {promedio}")
