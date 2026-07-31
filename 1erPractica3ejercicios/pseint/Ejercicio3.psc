Algoritmo Ejercicio3
	Escribir "Ingrese años de experiencia"
	Leer expe
	Si expe<0 Entonces
		Escribir "Error, revise..."
	SiNo
		Escribir "Ingrese nivel de ingles(A-Avanzado,I-Intermedio,B-Basico)"
		Leer lvl
		Si lvl="A" O lvl="I" O lvl="B" Entonces
			Escribir "Nivel de ingles Guardado"
			Escribir "Tiene titulo universitario? (S/N)"
			Leer title
			Si title="S" o title="N" Entonces
				Escribir "Caracter Guardado"
				
				Si expe>=5 Y lvl="A" Y title="S" Entonces
					Escribir "Clasificado en: SENIOR"
				SiNo
					Si (expe>=3 Y expe<=4) Y (lvl="A" O lvl="I") Entonces
						Escribir "Clasificado en: MID-LEVEL"
					SiNo
						Si (expe>=1 O expe<=2) Entonces
							Escribir "Clasificado en: JUNIOR"
						SiNo
							Escribir "Clasificado en: No legible"
						FinSi
					Finsi
				FinSi				
			Sino
				Escribir "Caracter invalido,revise..."
			FinSi
		SiNo
			Escribir "Nivel invalido"
		FinSi
	FinSi

FinAlgoritmo
