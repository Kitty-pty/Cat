print("Bienvenido a la calculadora de utilidad")
Costo = float(input("¿Cual es es tu precio a costo?"))
Utilidad = float(input("¿Cual es el porentaje de utilidad deseado?"))
Venta=round((Costo/(1-(Utilidad/100))))

print(f"El precio de venta es {Venta} ")
