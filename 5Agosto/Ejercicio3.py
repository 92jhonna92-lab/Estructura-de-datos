materias={"Lunes":["Estructura","Ingles"],
          "Martes":["Telematica","Diseño"],
            "Miercoles":["Desarrollo Personal","Ensamblaje"],
            "Jueves":["Estructura","Telematica"],
            "Viernes":["Sistemas operativos"]}
for dia in ["Lunes","Martes","Miercoles","Jueves","Viernes"]:
    print(f"Dia: {dia}")

    for materia in materias[dia]:
        print(f"materia-{materia}")

