def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar ...")


def leerValHora(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Valor de las horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Valor de las Horas inválidas")
            continue

def leerHoras(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Horas mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Horas inválidas")
            continue
        
def leerNom(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error Nombre inválido.")
                continue
            return n
        except Exception as e:
            print("Ha sucedido un Error: ", e)
            continue
        
def leerId(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                msgError("Error. Id mayor que 0")
                continue
            return n
        except ValueError:
            msgError("Error. Id inválido")
            continue

def agregarEmpleado(lstEmpl):
    pass
    # print("\n\n*** 1. Agregar empleado - ACME ***\n")
    
    # id = leerId("Id del empleado: ")
    # nom = leerNom("Nombre del empleado: ")
    # hora = leerHoras("Horas trabajadas: ")
    # valh = leerValHora("Valor de la Hora trabajada: ")
    
    # datempl = [id, nom, hora, valh]
    # lstEmpl.append(datempl) 
    # print(lstEmpl)
    # input()


def buscarEmpleado(lstEmpl):
    while True:
        try:
            lstEmpl=[[123, 'Mauricio', 5, 60000], [124, 'Manuel', 12, 50000]]
            print("Desea:\n\
            1. Ver la cantidad todal de empreados\n\
            2. Ver la lista de los empleados en lista\n\
            3. Buscar por id\n\
            4. Regresar\n")
            op=int(input("¿Qué desea hacer? "))
            # "Ver en lista"
            if op == 1:
                print("\n\nTotal de empleados registrados:", len(lstEmpl),"\n\n")
                input("Presione enter para continuar.")
                break
            elif op == 2:
                print("\nSeleccionó: Ver en lista \n")
                for i in range(0,len(lstEmpl)):
                    print("Empleado:", (i+1), lstEmpl[i][1])
                input("Presione enter para continuar.")
                break
            elif op == 3:
                print("Seleccionó: Buscar por id")
                bus=int(input("Ingrese el id del empleado que va a buscar: "))
                esta=False
                for i in range(0,len(lstEmpl)):
                    print(lstEmpl[i][0])
                    if lstEmpl[i][0] ==bus:
                        print("El id de ",bus, "fue encontrado.")
                    else:
                        print("No se encontró")
                    input()
                    break
            elif op == 4:
                break
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 3).")
            continue
        # "Buscar por id"
        # "Modificar" 
        # print(f"Total de empleados:",len(lstEmpl))


def modificarEmpleado(lstEmpl):
    lstEmpl=[[123, 'Mauricio', 5, 60000], [124, 'Manuel', 12, 50000]]
    pass

def menu():
    while True:
        try:
            print("\n\n*** NOMINA ACME ***")
            print("\tMENU")
            print("1- Agregar empleado\n\
2- Modificar empleado\n\
3- Buscar empleado\n\
4- Eliminar empleado\n\
5- Listar empleados\n\
6- Listar nómina de un empleado\n\
7- Listar nómina de todos los empleados\n\
8- Salir\n")
            op = int(input("\t>> Escoja una opción (1-8)?"))
            if op < 1 or op > 8:
                msgError("Error. Opción Inválida (de 1 a 8).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 8).")
            continue
        
def main():
    lstEmpl = []
    while True:
        op = menu()
        if op == 1:
            agregarEmpleado(lstEmpl)
        elif op == 2:
            modificarEmpleado(lstEmpl)
        elif op == 3:
            buscarEmpleado(lstEmpl)
        # colocar otras opciones
        elif op == 8:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
main()