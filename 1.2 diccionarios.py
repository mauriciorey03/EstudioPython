meses={'enero':1,'febrero':2}
print(meses, " >> diccionario")

#VER
print(meses['enero']," >> resultado de la ubicación dentro del diccionario")

#AGREGAR
meses['marzo']=3
print(meses," >> sumado marzo")

#BORRAR
del meses['febrero']
print(meses," >> eliminado febrero")
