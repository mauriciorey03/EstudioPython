dicCat = {}
dicCat = {1: 10000, 2: 20000, 3: 30000, "2": "Dos", 4: [15000, 25000]}
# dicCat.clear() 
dicCat[4].append(35000)  #AGREGA A LA POSICIÓN 4 (LISTA, EL ELEMENTO 35000)
print(dicCat)
#modificar
dicCat[2] = 24000 #MODIFICA EL VALOR DE LA KEY 2
print(dicCat, "DIC")
dicCat["Un valor"]=41 #AGREGA UNA LLAVE AL DICCIONARIO
print(dicCat, "DIC2")

print(dicCat.get("2")) #DEVUELVE EL VALOR DE LA "LLAVE"
del dicCat["2"]
print(dicCat.get("2", "Devuelve el mensaje si no existe"))
print(dicCat.get(2, "Ejemplo")) #SI EL VALOR EXISTE, DEVUELVE EL VALOR Y NO EL MENSAJE

miDiccionario={'manzana':430, 'bananas':312, 'peras':217}


print(miDiccionario.keys()) #MUESTRA LAS LLAVES  manzan, banana, peras

print(miDiccionario.values()) #MUESTRA LOS VALORES  430,312,217

print(miDiccionario.items()) #MUESTRA KEY:VALUE

print(miDiccionario['manzana'])

thisdict =	{"brand": "Ford","model": "Mustang","year": 1964,"prices":[1200,1300,1400]}
for x, y in thisdict.items():
    print(x, y)

for elem in thisdict["prices"]:
    print(elem)

