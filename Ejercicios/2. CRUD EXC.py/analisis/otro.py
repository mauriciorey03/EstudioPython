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
nombre=input('digite la marca que quiere modificar: ')

for i in range (0,cantidad):
    if nombre==ruta[i]['marca']:
        print(' '*4,ruta[i]['marca'])
        print(' '*4,ruta[i]['linea'])
        print(' '*4,ruta[i]['modelo'])
        print(' '*4,ruta[i]['equipamiento'])
        marca=input('ingrese nueva marca: ')
        #ruta[i]['marca']=marca
        ruta[i]={
        'marca':marca,
        }
        print(ruta[i]['marca'])

