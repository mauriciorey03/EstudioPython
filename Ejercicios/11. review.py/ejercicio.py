import json
with open('archivo.txt','r') as f:
    lineas = f.readlines()

addClient={}
addClient['vendedores']=[]

for i in lineas[1:]:
    lista=i.replace("\n","").split(", ")
    addClient['vendedores'].append([{'Apellido': lista[0], 'id': lista[1], 'saldo':[lista[2:]]}])

with open('resultado.json','w') as archivo:
    json.dump(addClient,archivo,indent=4)