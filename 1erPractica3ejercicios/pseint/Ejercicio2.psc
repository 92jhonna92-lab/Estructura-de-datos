Algoritmo Ejercicio2
	Escribir "Seleccione tipo de cliente(A,B,C)"
	Leer cliente
	Si cliente="A" o cliente="B" o cliente="C" 
		
		Si cliente="A" Entonces
			Escribir "Ingrese Monto total"
			Leer MontoTotal
			Si MontoTotal>1000 Entonces
				descuento=MontoTotal*0.2
				Escribir "El descuento es:", descuento
			SiNo
				descuento=MontoTotal*0.15
				Escribir "El descuento es:",descuento
			FinSi
		FinSi
		Si cliente="B" Entonces
			Escribir "Ingrese Monto total"
			Leer MontoTotal
			Si MontoTotal>1000 Entonces
				descuento=MontoTotal*0.1
				Escribir "El descuento es:", descuento
			SiNo
				descuento=MontoTotal*0.05
				Escribir "El descuento es:",descuento
			FinSi
		FinSi
		Si cliente="C" Entonces
			Escribir "No recibe ningun descuento"
		FinSi
	SiNo
		Escribir "Opcion invalida"
	FinSi
	
FinAlgoritmo
