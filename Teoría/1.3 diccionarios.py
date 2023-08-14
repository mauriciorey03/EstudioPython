meses={'enero':1,'febrero':2}
print(meses, "\n\t >> diccionario\n")

#VER
print(meses['enero'],"\n\t >> resultado de la ubicación dentro del diccionario\n")

#AGREGAR
meses['marzo']=3
print(meses,"\n\t >> sumado marzo\n")

#BORRAR
del meses['febrero']
print(meses,"\n\t >> eliminado febrero\n")


