c=int(input("Ingrese hasta que numero desea multiplicar: "))
for a in range(1,c+1):
    for b in range(1,11):
        mult=a*b
        print(f"{a} x {b}= {mult}")