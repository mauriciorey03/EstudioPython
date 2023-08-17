import json
import os
os.system("cls")
def leerDatos():
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
        misDatos = json.load(miAlmacen)
        miListadeAutos = misDatos["autostore"]["autos"]
    i=0
    for auto in miListadeAutos:
        i+=1
        print (i, " ", auto, "\n")

def mostrarUno(i):
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]
    print(miAuto)

def mostrarEquipamiento(i):
    i-=1
    with open('AutoShopping.json', encoding="utf-8") as miAlmacen:
            misDatos = json.load(miAlmacen)
            miAuto = misDatos["autostore"]["autos"][i]["equipamiento"]
    print(miAuto)

def agregarAuto():
    auto = {
        "marca":"Chevrolet",
        "linea": "Monza",
        "modelo": "2000",
        "precio": "9000"
    }
    n=int(input("Cuántos elementos ?"))
    if (n==0):
        auto["equipamiento"] = "Sin Equipamiento "
    else:
        if (n==1):
            equipamiento=input("Ingrese el equipo: ")
        else:
            equipamiento=[]
            for i in range (n):
                equipamiento.add(input("Ingrese el equipo: "))
    auto["equipamiento"]=equipamiento          

leerDatos()
for i in range (2):
    indice=int(input("Cuál desea ver? "))
    mostrarUno(indice)
    mostrarEquipamiento(indice)
    input()

agregarAuto()
