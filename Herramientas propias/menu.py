def menu():
    while True:
        try:
            print("\n\n*** TITULO ***")
            print("\tMENU")
            print("1- Agregar usuario\n\
2- Modificar usuario\n\
3- Buscar usuario\n\
4- Eliminar usuario\n\
5- Listar usuarios\n\
6- Salir\n")
            op = int(input("\t>> Escoja una opción (1-6): "))
            if op < 1 or op > 6:
                print("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            print("Error. Opción Inválida (de 1 a 6).")
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
        elif op == 6:
            print("\n", "Gracias por usar el programa... Adios...".center(80))
            break
    

# Programa Principal
main()