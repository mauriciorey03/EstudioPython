import json
def readCars():
    with open('cars.json','r',encoding='utf-8') as cars:
        data = json.load(cars)
        rutaLectura = data['autostore']['autos']
    return rutaLectura

def writeCars(dat):
    with open('cars.json','w') as archivo:
        json.dump(dat,archivo,indent=4,ensure_ascii=False)
    return None

ruta=readCars()

def ConvertirStrLst(evaluar):
    if type(evaluar) is list:
        s = ', '.join(evaluar)
    elif type(evaluar) is str:
        s=evaluar
    return s


def showCars(arg):
    contador=0
    print("{:^2}|{:^9}|{:^7}|{:^7}|{:^7}|{:^50}".format("#","MARCA","LÍNEA","MODELO","PRECIO","EQUIPAMIENTO"))
    for elem in arg:
        contador += 1
        equi=ConvertirStrLst(elem['equipamiento'])
        print("{:^2}|{:^9}|{:^7}|{:^7}|{:^7}|{:^50}".format(f"{contador}", elem['marca'], elem['linea'],elem['modelo'],elem['precio'],f"{equi}"))
    return None

showCars(ruta)

    #     print(elem['marca'])
    #     print(elem['linea'])
    #     print(elem['modelo'])
    #     print(elem['precio'])
    #     print(elem['equipamiento'][0:])

cantidad=len(ruta)
print(cantidad)
for i in range (0,cantidad):
    print(ruta[i])
    #print(ruta[i-1].get('marca'))

pregunta=int(input('Desea agregar el vehiculo num?'))

print(ruta[pregunta-1].get('marca'))


print('funciona')
autos={}
cont = 0
cod = True
while cod:    
    print("\nIngrese los datos del vehículo  #", cont + 1)
    pregunta=input('Desea agregar un vehículo? [S]i - [N]o: \n')
    if pregunta.lower() == "n":
        cod=False
        break
    elif pregunta.lower()=="s":        
        cont += 1
    #     print(elem['marca'])
    #     print(elem['linea'])
    #     print(elem['modelo'])
    #     print(elem['precio'])
    #     print(elem['equipamiento'][0:])

        marca = input("Ingrese el marca: ")
        raza = input("Ingrese la raza: ")
        talla = input("Ingrese el talla: ")
        precio = int(input("Ingrese el precio: "))
        servicios = input("Ingrese el servicios: (Separados")
        {"marca":marca,"linea": "Beat","modelo": "2020","precio": "10000","equipamiento": ["Luces Exploradoras"]
            }
        
        autos['pets'].append({ "tipo" : tipo, "raza" : raza, "talla" : talla, "precio":precio, "servicios":servicios})



print("Creando archivo...")