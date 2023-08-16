import json
with open('pets.json') as mascotas:
    data = json.load(mascotas)

for num in data['pets']:
    print('tipo: ', num['tipo'])
    print('raza: ', num['raza'])
    print('talla: ', num['talla'])
    print('precio: ', num['precio'])
    print('servicios: ', num['servicios'])


masco={}
masco['pets']=[]
cont = 0
cod = True
while cod:
    
    print("\nIngrese los datos del pets  #", cont + 1)
    pregunta=input('Desea agregar una mascota? [S]i - [N]o: \n')
    if pregunta.lower() == "n":
        cod=False
        break
    elif pregunta.lower()=="s":        
        cont += 1
        tipo = input("Ingrese el tipo: ")
        raza = input("Ingrese la raza: ")
        talla = input("Ingrese el talla: ")
        precio = int(input("Ingrese el precio: "))
        servicios = input("Ingrese el servicios: (Separados")
        
        
        masco['pets'].append({ "tipo" : tipo, "raza" : raza, "talla" : talla, "precio":precio, "servicios":servicios})
    
    with open('pets.json','w') as archivo:
        json.dump(masco,archivo,indent=4)    


print("Creando archivo...")

