##Ejercicio3
expe=int(input("Ingrese años de experiencia: "))
if expe<0:
    print("ERROR, Revise...")
else:
    lvl=input("Ingrese nivel de ingles(A=Avanzado, I=Intermedio,B=Basico): ")
    lvl=lvl.upper()
    if lvl=="A" or lvl=="I" or lvl=="B":
        print("Nivel de ingles guardado")
        title=input("Tiene titulo universitario?(S/N): ")
        title=title.upper()
        if title=="S" or title=="N":
            print("Caracter guardado")
            if expe>=5 and lvl=="A" and title=="S":
                print("Clasificado en: SENIOR")
            else:
                if (expe>=3 and expe<=4) and (lvl=="A" or lvl=="I"):
                    print("Clasificado en: MID-LEVEL")
                else:
                    if(expe>=1 or expe<=2):
                        print("Clasificado en: JUNIOR")
                    else:
                        print("Clasificado en: NO LEGIBLE")
        else:
            print("Caracter invalido, revise...")
    else:
        print("Nivel de ingles invalido, revise...")
