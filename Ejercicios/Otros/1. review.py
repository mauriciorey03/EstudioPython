hr=int(input("Ingrese la hora original "))
min=int(input("Ingrese los min "))
minAdd=int(input("Ingrese nuevos min "))

minHora=hr*60
totalMin=min+minHora+minAdd
nuevaHora=totalMin//60
nuevoMin=totalMin%60

print("Hora ingresada", hr)
print("Min ingresados", min)
print("Mins añadidos", minAdd)

print(f"Nueva hora {nuevaHora}:{nuevoMin:0<2}")
