# #EJERCICIO 1
# dias=int(input("Establezca la cantidad de días "))
# kms=int(input("Defina la cantidad de kms del viaje "))

# valorkm=2500
# precio=valorkm*kms

# if (dias > 7) and (kms > 800):
#     preciods=(precio-(precio*0.3))
#     print(f"¡Felicidades tiene un descuento del 30%! \nEl valor de su ticket es de ${preciods:,.0f}")
# else:
#     print(f"El valor de su ticket es de ${precio:,.0f}")

#EJERCICIO 2
dd=int(input("Ingrese el día: "))
mm=int(input("Ingrese el mes: "))
aa=int(input("Ingrese el año: "))

dd=dd+1

if (aa % 4 == 0) or (aa % 100 == 0) or (aa % 400 == 0):
    bisiesto=True
else:
    bisiesto=False
    
if (mm==1) or (mm==3) or (mm==5) or (mm==8) or (mm==10):
    if dd>31 and mm==12:
        dd=1
        mm=1
        aa=aa+1
    elif dd>31:
        dd=1
        mm=mm+1
elif (mm== 4) or (mm== 6) or (mm== 9) or (mm==11):
    if dd>30:
        dd=1
        mm=mm+1
elif (mm==2) and (bisiesto==True):
    if dd>29:
        dd=1
        mm=3
elif (mm==2) and (bisiesto==False):
    if dd>28:
        dd=1
        mm=mm+1
else:
    print("Por favor compuebe que el mes o el día este correctamente")

print(f"La próxima fecha será: {dd} del mes {mm} del {aa}.")

#EJERCICIO 3 - EDGAR MAURICIO MEZA REY
# kg=float(input("Put your weight in Kg "))
# alt=float(input("Put your heigh in Mts "))

# lb=(kg*0.45359237)
# inch=(alt*0.0254)
# bmi=(lb/(inch*inch))

# if (bmi < 18.5): 
#     result="Underweight"
# elif (bmi > 18.5 and bmi < 24.9): 
#     result="Normal"
# elif (bmi > 25 and bmi < 39.9):
#     result="Overweight"
# elif (30 < bmi): 
#     result="Obese"
# else:
#     result="Error. Try again."

# print(f"BMI is {bmi:,.2f}")
# print(result)