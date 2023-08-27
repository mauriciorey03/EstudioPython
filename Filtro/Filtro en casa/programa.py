import json
import os

def leerManuales():
    with open('manuales.json','r',encoding='utf-8') as manuales:
        data = json.load(manuales)
    return data

def escribirManualesJSON(escribir):
    with open('manuales.json','w') as archivo:
        json.dump(escribir,archivo,ensure_ascii=False,indent=4)    
    print("Creando archivo...")

#estructura:
#{lenguaje: dict{'author': 'Valor , 'paginas':65, 'temas':['titulo':'tema','clasificación':1]}}
def crearManuales():
    pass

def modificarManuales():
    pass

def eliminarLenguaje():
    pass

def eliminarTemas():
    pass


def Texto ():
    pass

def listarManuales():
    pass

def escribirTXT():
    pass

def menu():
    while True:
        try:
            print("=====* MENÚ PRINCIPAL *=====\n\
    1. Crear\n\
    2. Modificar\n\
    3. Eliminar\n\
    4. Listar\n\
    5. Generar informe de datos.txt")
            op = int(input(">> Escoja una opción (1-5): "))
            if op < 1 or op > 5:
                print("Error. Opción Inválida (de 1 a 5).")
                continue
            return op
        except ValueError:
            print("Error. Opción Inválida (de 1 a 5).")
            continue


def main():
    while True:
        op = menu()
        if op == 1:
            print("\tSeleccionó: 1")
            crearManuales()
        elif op == 2:
            print("\tSeleccionó: 2")
            modificarManuales()
        elif op == 3:
            print("\tSeleccionó: 3")
            eliminarLenguaje()
        elif op == 4:
            print("\tSeleccionó: 4")
            listarManuales()
        elif op == 5:
            print("\tSeleccionó: 5")
            escribirTXT()
            break

# Programa Principal
main()