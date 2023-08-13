def menu():
    while True:
        try:
            print("\n\n*** TITULO ***")
            print("\tMENU")
            print("1- Agregar empleado\n\
2- Modificar empleado\n\
3- Buscar empleado\n\
4- Eliminar empleado\n\
5- Listar empleados\n\
6- Listar nómina de un empleado\n\
7- Listar nómina de todos los empleados\n\
8- Salir\n")
            op = int(input("\t>> Escoja una opción (1-8): "))
            if op < 1 or op > 8:
                print("Error. Opción Inválida (de 1 a 8).")
                continue
            return op
        except ValueError:
            print("Error. Opción Inválida (de 1 a 8).")
            continue
        
def main():
    lstEmpl = [] # lst vacía
    while True:
        op = menu()
        if op == 1:
            print("Seleccionó: 1")
            # función -> agregarEmpleado(lstEmpl)
        elif op == 2:
            print("Seleccionó: 2")
            # función ->  modificarEmpleado(lstEmpl)
        elif op == 3:
            print("Seleccionó: 3")
            # función -> buscarEmpleado(lstEmpl)
        # colocar otras opciones
        elif op == 8:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
main()