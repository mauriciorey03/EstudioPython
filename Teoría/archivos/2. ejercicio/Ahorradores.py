import json
with open('Ahorradores.json') as usuarios:
    clientes = json.load(usuarios)

addClient={}
addClient['clientes']=[]
consecutivo=0
for elem in clientes['cliente']:
    if elem['Saldo'] > 35_000_000:
        consecutivo+=1
        addClient['clientes'].append({'consecutivo': consecutivo, 'numCuenta': elem['NumCuenta'], 'saldo':elem['Saldo']})

with open('Dian.json','w') as archivo:
    json.dump(addClient,archivo,indent=4)