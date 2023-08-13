#EJERCICIO 1
# emp=input("Ingrese el nombre del empleado: ")
# hor=int(input("Ingrese el total de horas de trabajo: "))

# valHor=float(20000)
# sueBru=int(valHor*hor)
# desEps=int(sueBru*0.04)
# desPen=int(sueBru*0.04)
# desNetEps=int(sueBru-desEps)
# desNetPen=int(sueBru-desPen)
# sueNet=int(sueBru-(desPen+desEps))

# print("\n","-"*20)
# print("Liquidación del sueldo del trabajador ", emp)
# print(f"Total de horas trabajadas: {hor}")
# print(f"Sueldo bruto: ${sueBru}")
# print(f"Descuento EPS ${desEps}, total ${desNetEps}")
# print(f"Descuento Pensión ${desPen}, total ${desNetPen}")
# print(f"Total de salario bruto ${sueNet}")

#EJERCICIO 2
hh = int(input("Ingresa la cantidad de horas (máximo 24): "))
mm = int(input("Ingresa la cantidad de minutos: "))
mms = int(input("Ingresa la cantidad de minutos a recalcular: "))

min_hh=hh*60
MinTotal=min_hh+mm+mms
nueHora=MinTotal//60
nueMin=MinTotal%60

print(f"Hora: {hh}:{mm}")
print("Minutos agregados:",mms)
print(f"La nueva hora es {nueHora}:{nueMin:0<2}")

#EJERCICIO 3
# nota=float(input("Ingrese una nota entre 0.0 y 5.0: "))
# curNot=(nota*0.8)+1
# print(f"El valor de la curva de 8 es de {curNot:.2f}")