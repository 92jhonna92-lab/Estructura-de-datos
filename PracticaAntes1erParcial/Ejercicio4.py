num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
op= input("Ingrese la operacion deseada: (+,-,*,/)")
match op:
    case "+":
        print("Eligio suma")
        suma=num1+num2
        print("La suma de los 2 numeros es: ", suma)
    case "-":
        print("Eligio resta")
        resta=num1-num2
        print("La resta de los 2 numeros es: ", resta)
    case "*":
        print("Eligio multiplicacion")
        mult=num1*num2
        print("La multiplicacion es: ", mult)
    case "/":
        print("Eligio division")
        div=num1/num2
        print("La division es: ",div)
    case _:
        print("Opcion no valida")
        exit()