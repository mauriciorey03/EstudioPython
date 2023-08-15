import json

data={}
data['clients']=[]

data['clients'].append({
    'first_name':'Theodoric',
    'last_name':'Rivers',
    'age':36,
    'amount':1.11
})

data['clients'].append({
    'first_name':'Mauricio',
    'last_name':'Rivers',
    'age':27,
    'amount':3.11
})

with open('misdatos.json','w') as archivo:
    json.dump(data,archivo,indent=16)