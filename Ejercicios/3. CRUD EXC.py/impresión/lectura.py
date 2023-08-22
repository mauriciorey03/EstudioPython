import json
import os
os.system("cls")

def leerDatos():
    with open('ciudades.json', encoding="utf-8") as data:
        misDatos = json.load(data)
        city = misDatos["Departamentos"]
    return city


ruta=leerDatos()
#print(ruta[0]['Ciudades'][0]['nomCiudad'])

def leerCiudades():
    for i in ruta:
        for x in i['Ciudades']:
            print(x['nomCiudad'])

def leerDepartamentos():
    for i in ruta:
        listDept=i['nomDepartamento']
    return listDept

def elimCiudad():
    elim = input("Cuál ciudad desea eliminar")
    for i in ruta:
        for x in i['Ciudades']:
            if elim == x['nomCiudad']:
                i['Ciudades'].remove(x)
                break
    leerCiudades()

def elimDepartamentos():
    elim = input("Cuál Departamento desea eliminar")
    for i in ruta:
        if elim == i['nomDepartamento']:
            ruta.remove(i)
            print("SE ELIMINÓ")#i['Ciudades'].remove(x)
            break
        else:
            print("El departamento no existe")
    leerDepartamentos()

def adicionarCiudad():
    addCiud = input("a cuál Departamento desea agregarle la ciudad? ")
    while addCiud.title() not in 
        if addCiud.title() in i['nomDepartamento']:
            n=i['idDep']
    idCiudad = int(input('Ingrese un código: '))
    verificador = asigCodigo()
    while idCiudad in verificador:
        idCiudad = int(input('El código ya está, ingrese un nuevo código: '))
    nombreCiudad = input('Ingrese el nombre de la ciudad: ')
    image = nombreCiudad.lower()
    ciudad = {
        'idCiudad':idCiudad,
        'nomCiudad':nombreCiudad.title(),
        'imagen':(image+".jpg"),
        'Coordenadas':{'lat':4,"lon":72}
        }
    ruta[n]['Ciudades'].append(ciudad)


# TODO:CREAR UN DEPARTAMENTO
# ADICIONAR UNA CIUDAD A UN
def asigCodigo():
    codigos=[]
    for i in ruta:
        for n in i['Ciudades']:
            codigos.append(n['idCiudad'])
    return codigos

adicionarCiudad()
print(ruta)
# {
# 	"Departamentos":
# 	[{"iDep":1,"nomDepartamento":"Santander","Ciudades":[
# {"idCiudad":1,"nomCiudad":"Bucaramanga","imagen":"bucaramanga.jpg","coordenadas":{"lat":4,"lon":72}},
# {"idCiudad":1,"nomCiudad":"Barracabermeja","imagen":"Barracabermeja.jpg","coordenadas":{"lat":4,"lon":72}}
# ]}]}


