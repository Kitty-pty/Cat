#Calculadora de pendiente de techo
import math

print ("Bienvenido a tu calculadora de pendiente de techo")
Amax= float (input ("Introduce altura máxima "))
Amin= float (input ("Introduce altura mínima "))
Ancho= float (input ("Introduce el ancho del galpón/galera "))
Pendiente= round ((((Amax-Amin)/(Ancho/2))*100),2)
Angulo=round(math.degrees(math.atan((Amax-Amin)/(Ancho/2))),2)

print (f"La pendiente es {Pendiente}%")

print (f"El ángulo es {Angulo}°")

