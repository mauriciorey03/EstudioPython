import json
import os
os.system("clear")

def leerDatos():
    with open('ciudades.json', encoding="utf-8") as data:
        misDatos = json.load(data)
        city = misDatos["Departamentos"]
    return city


ruta=leerDatos()
print(ruta[0]['Ciudades'][0]['nomCiudad'])

def leerCiudades():
    contador = 0
    for i in ruta:
        for x in i['Ciudades']:
            contador+=1
            print(contador,x['nomCiudad'])

def leerDepartamentos():
    for i in ruta:
        print(i['nomDepartamento'])

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
    leerDepartamentos()

print(ruta)
# {
# 	"Departamentos":
# 	[{"iDep":1,"nomDepartamento":"Santander","Ciudades":[
# {"idCiudad":1,"nomCiudad":"Bucaramanga","imagen":"bucaramanga.jpg","coordenadas":{"lat":4,"lon":72}},
# {"idCiudad":1,"nomCiudad":"Barracabermeja","imagen":"Barracabermeja.jpg","coordenadas":{"lat":4,"lon":72}}
# ]}]}



# def agregarAuto():
#     auto = {
#         "marca":"Chevrolet",
#         "linea": "Monza",
#         "modelo": "2000",
#         "precio": "9000"
#     }
#     n=int(input("Cuántos elementos ?"))
#     if (n==0):
#         auto["equipamiento"] = "Sin Equipamiento "
#     else:
#         if (n==1):
#             equipamiento=input("Ingrese el equipo: ")
#         else:
#             equipamiento=[]
#             for i in range (n):
#                 equipamiento.add(input("Ingrese el equipo: "))
#     auto["equipamiento"]=equipamiento          
