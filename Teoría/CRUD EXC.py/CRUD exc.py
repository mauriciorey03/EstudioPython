# Simulacro CICLO 1
# Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:
# 	1. Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios
# 	2. Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio
# 	3. Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios
# 	4. Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por 	índice)
# 	5. Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)
import json

def menu():
    while True:
        try:
            print("\n\n*** EL CRUD DE MASCOTAS ***")
            print("1- Mostrar todas las mascotas\n\
2- Crear nueva mascota\n\
3- Mostrar los datos de Mascotas\n\
4- Actualizar los datos de una mascota\n\
5- Eliminar una mascota de la tienda\n\
6- Salir\n")
            op = int(input("\t>> Escoja una opción (1-6): "))
            if op < 1 or op > 6:
                print("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            print("Error. Opción Inválida (de 1 a 6).")
            continue

def leerMascotas():
    with open('pets.json','r',encoding='utf-8') as mascotas:
        data = json.load(mascotas)
    return data

def escribirMascotas(escribir):
    with open('pets.json','w') as archivo:
        json.dump(escribir,archivo,ensure_ascii=False,indent=4)    
    print("Creando archivo...")

# 	1. Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios
def mostrarMascotas():
    data = leerMascotas()
    contador=0
    print("# -- tipo -- raza -- precio -- servicios")
    for num in data['pets']:
        contador += 1
        print(contador, num['tipo'],num['raza'],num['talla'],num['servicios'])
    return None

#2. Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio
def crearMascotas():
    masco=leerMascotas()
    cont = 0
    cod = True
    while cod:
        
        print("\nIngrese los datos de la mascota  #", cont + 1)
        pregunta=input('Desea agregar una mascota? [S]i - [N]o:  \n')
        if pregunta.lower() == "n":
            cod=False
            break
        elif pregunta.lower()=="s":        
            cont += 1
            tipo = input("Ingrese el tipo: ")
            raza = input("Ingrese la raza: ")
            talla = input("Ingrese el talla: ")
            precio = int(input("Ingrese el precio: "))
            servicios=[]
            while True:
                add = input("Ingrese el servicios: ")
                pre=input("Desea agregar otro [S]i -- [N]o")
                pre.lower()
                servicios.append(add)
                if pre == "s":
                    continue
                elif pre == "n":
                    break            
            masco['pets'].append({ "tipo" : tipo, "raza" : raza, "talla" : talla, "precio":precio, "servicios":servicios})
        
        escribirMascotas(masco)
    return

# 	3. Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios
def buscarMascota():
    data=leerMascotas()
    num=int(input("Ingrese el número de la lista principal, de la mascota que desea buscar: "))
    if num != None:
        print("El animal es un: ",data['pets'][num]['tipo'])
        print(data['pets'][num]['raza'],data['pets'][num]['precio'],data['pets'][num]['servicios'])
    else:
        print("\nLa mascota no figura en la lista")
    input("Presione cualquier tecla para continuar ...")

def actualizarMascota():
    data=leerMascotas()
    num=int(input("Ingrese el número de la mascota que desea modificar: "))
    if num != None:
        print("Va a modificar la información de: ", data['pets'][num]['tipo'])
        print("Cual valor desea modificar:\n\
            \t1.Raza\n\
            \t2.Talla\n\
            \t3.Precio\n\
            \t4.Servicio\n\
            o presione cualquier tecla para cancelar")
        newMod=int(input("Seleccione una opc: "))
        if newMod==1:
            raza = input("Ingrese la nueva raza: ")
            data['pets'][num]['raza']=raza
            print("Se modificó la raza: ", raza)
        elif newMod==2:
            talla = input("Ingrese la nueva talla: ")
            data['pets'][num]['talla']=talla
            print("Se modificó la talla: ", talla)
        elif newMod==3:
            precio = int(input("Ingrese el nuevo precio: "))
            data['pets'][num]['precio']=precio
            print("Se modificó el precio: ", precio)
        elif newMod==4:
            servicios = input("Ingrese el servicios: ")
            data['pets'][num]['precio']=precio
            print("Se modificó el precio: ", precio)
        else:
            print("Se cancelo la modificación.")
        escribirMascotas(data)
    else:
        print("\nLa mascota no figura en la lista")
    input("Presione cualquier tecla para continuar ...")


# 	5. Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)
def eliminarMascota():
    mostrarMascotas()
    print()
    data=leerMascotas()
    num=int(input("Ingrese el número de la mascota "))
    if num != None:
        print("\nNombre:", data['pets'][num]['tipo'])
    si=input("Está seguro que desea eliminarlo? ([S]i - [N]o)"  )
    if si.lower()=="Si":
        del data['pets'][num]
        print("La mascota se eliminó satisfactoriamente.")
    else:
        print("\nLa mascota no figura en la lista")
    input("Presione cualquier tecla para continuar ...")



def main():
    while True:
        leerMascotas()
        op = menu()
        if op == 1:
            print("Seleccionó: 1")
            mostrarMascotas()
        elif op == 2:
            print("Seleccionó: 2")
            crearMascotas()
        elif op == 3:
            print("Seleccionó: 3")
            buscarMascota()
        elif op == 4:
            print("Seleccionó: 4")
            actualizarMascota()
        elif op == 5:
            print("Seleccionó: 5")
            eliminarMascota()
        elif op == 6:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
main()