Algoritmo Ejercicio1
	Escribir "Ingrese monto de compra:"
	Leer MontoC
	Si MontoC<=0 Entonces
		Escribir "Monto no valido, revise...."
	FinSi
	si MontoC>500 Entonces
		descuento=MontoC*0.1
		MontoTotal=MontoC-descuento
		Escribir "El descuento es:", descuento
		Escribir "Monto final de la compra es:", MontoTotal
	SiNo
		Escribir "No aplica descuento"
	FinSi

FinAlgoritmo
