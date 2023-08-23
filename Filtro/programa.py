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
    data = leerManuales()
    print("========* CREACIÓN *========")
    lenguaje = input("Ingrese el lenguaje: ")
    author = input("Ingrese el autor: ")
    paginas= int(input("Ingrese la cantidad de paginas:"))
    incluir=True
    temas=[]
    while incluir:
        ask=input("\tDesea incluir un tema? \n1. Si \n2. No \nEscriba el número: ")
        if ask.lower() == "2":
            incluir=False
            break
        elif ask.lower() == "1":
            title=input("Ingrese el título: ")
            clasifica=int(input("Ingrese la clasificación: "))
            dic_temas={'Titulo':title,'Clasificación':clasifica}
            temas.append(dic_temas)
            continue
    info={'author':author,'paginas':paginas,'temas':temas}
    if lenguaje not in data['manuales']:    
        data['manuales'][lenguaje]=info
        escribirManualesJSON(data)
    elif lenguaje in data['manuales']: 
        print("El lenguaje ya existe, compruebe si quiere modificar")
    print(data)
    return

def modificarManuales():
    data = leerManuales()
    print("Qué desea modificar\n\
    1. lenguaje\n\
    2. tema")
    mod = input("Ingrese el elemento que desea modificar: ")
    contador = 0
    if mod == "1":
        print("Lista de lenguajes: ")
        for lenguaje in data['manuales'].keys():
            print(lenguaje)
        viejo=input("Qué lenguaje desea cambiar? ")
        for lenguaje in data['manuales'].keys():
            if viejo == lenguaje:
                print('existe')
                cambiar=lenguaje
                nuevo=data['manuales'][lenguaje].copy()
                nombre=input("que nombre desea que sea ahora?")
        del data['manuales'][cambiar]
        data['manuales'][nombre]=nuevo
        escribirManualesJSON(data)
    if mod == "2":
        elim = input("Cuál tema desea eliminar? ")
        for lenguajes in data['manuales']:
            for temas in data['manuales'][lenguajes]['temas']:
                print(temas)
    return None

def eliminarLenguaje():
    data = leerManuales()
    print("========* ELIMINACIÓN *========")
    print('Qué lenguaje desea eliminar?')
    print()
    contador=0
    for lenguaje in data['manuales']:
        contador+=1
        print(contador, lenguaje)
    print()
    lnprograma=input("Escriba el nombre del lenguaje que desea eliminar como aparece en la lista: ")
    data['manuales'].pop(lnprograma)
    escribirManualesJSON(data)
    print("El lenguaje se eliminó satisfactoriamente.")
    print()
    return

def eliminarTemas():
    data = leerManuales()
    print("========* ELIMINACIÓN *========")
    print('Qué tema desea eliminar?')
    print()
    contador=0
    for lenguaje in data['manuales']():
        for temas in libros['temas']:
            list[lenguaje]
            contador+=1
            ubica=[contador,temas['Titulo']]
            print(f"{contador}  {temas['Titulo']}")
    print()
    for lenguaje,libros in data['manuales'].items():
        for temas in libros['temas']:
            elntema=input("Escriba el nombre del lenguaje que desea eliminar como aparece en la lista: ")
            if elntema== libros['temas']:
                del temas['temas']
    print("El tema se eliminó satisfactoriamente.")
    print()
    return


def Texto():
    data = leerManuales()
    contador=0
    print("========* LISTADO *========")
    print()
    for lenguaje,libros in data['manuales'].items():
        for temas in libros['temas']:
            contador+=1
            print("Manual ",f"{lenguaje}:, {temas} ")
    print()
    return

def listarManuales():
    data = Texto()
    contador=0
    print("========* LISTADO *========")
    print()
    for lenguaje,libros in data['manuales'].items():
        for temas in libros['temas']:
            contador+=1
            print(f"{contador} | {temas['Titulo']} escritó por {libros['author']} | {lenguaje} ")
    print()
    return

def escribirTXT():
    data = leerManuales()
    linea=str(data)
    archivoEscritura=open("texto.txt","w")
    archivoEscritura.write(linea)
    archivoEscritura.close()

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