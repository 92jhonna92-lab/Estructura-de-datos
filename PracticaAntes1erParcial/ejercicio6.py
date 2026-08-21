materias={"lunes":["ensamblaje","ingles"], "martes":["desarrollo","telematica"], "miercoles":["estructura","telematica"], "jueves":["ensamblaje"],
          "viernes":["estructura", "diseño"]}
for dia in ["lunes","martes", "miercoles", "jueves", "viernes"]:
    print(f"Dia {dia}")
    for materia in materias[dia]:
        print(f"Materias {materia}")
