#CONDICIONALES
if ( a > b ):
    elementos 
elif ( a == b ): 
	elementos 
else:
	elementos

#CICLO FOR
for i in ____:
    elementos

for i in range(10):
    print i

#CICLO WHILE
while (condición):
    elementos

x = 0 
while x < 10: 
    print x 
    x += 1


#f-string
print(f"El área es: {area**:.3f}**") 0.000
#funcion format()
print("El área es: **{:.2f}".format(area)**) 0.0
#f para mil
print(f"El valor de su ticket es de ${precio**:,.0f**}") 1.000

print(f"Hora: {hh}:{mm}")
print("Minutos agregados: ",mms)
print(f"Nueva hora: {nuehh}:{nuemm**:0>2**}") hh:00

#salto de línea \n
print("Hola \nmundo"):
"Hola
mundo"
#tabulador \t
print("\n")
"Hola     mundo"


#libreria math importa una libreria especial, ver documentación
import math
#---función
#-----ciel(var): permite redondear hacía arriba
math.ciel(variable)

#-----round(var,cantidad de digitos): viene por defecto, redondea con n cantidad de decimales
round(8.586,2) 
8.59
#-----ranged(inicial, limite-1, escalado)
range(0,10,2)
	print(0,2,4,6,8)