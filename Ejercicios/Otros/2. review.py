# Escribir un programa en el que a partir de una fecha introducida por teclado con
# el formato DIAMES-AÑO, se obtenga la fecha del día siguiente.
# Para realizar el cálculo de forma correcta se debe tener en cuenta que hay meses
# con 30 días y otros con 31 y que febrero puede tener 29 si es bisiesto el año.

dd = int(input("Inserte el día: "))
mm = int(input("Inserte el mes: "))
aa = int(input("Inserte el el año: "))

if aa % 4 == 0 or aa % 100 == 0 or aa % 400 == 0:
    bisiesto=True
else:
    bisiesto=False

if mm==1 or mm==3 or mm==4 or mm==7 or mm==8 or mm==10:
    if dd<31:
        dd=dd+1
    elif dd==31:
        dd=1
        mm=mm+1
elif mm==4 or mm==6 or mm==9 or mm==11:
    if dd<30:
        dd=dd+1
    elif dd==30:
        dd=1
        mm=mm+1
elif mm==2 and bisiesto==True:    
    if dd<29:
        dd=dd+1
    elif dd==29:
        dd=1
        mm=mm+1
elif mm==2 and bisiesto==False:
    if dd<28:
        dd=dd+1
    elif dd==28:
        dd=1
        mm=mm+1
elif mm==12 and dd==31:
    dd=1
    mm=1
    aa=aa+1


print(f"{dd:0>2}/{mm:0>2}/{aa}")