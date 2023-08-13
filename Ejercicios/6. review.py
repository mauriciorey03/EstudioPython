#EJERCICIO REVIEW - 1 - EDGAR MAURICIO MEZA REY
while True:
    try:
        fecha = input("Cuando fue tu nacimiento en formato dd/mm/aaaa: ")
        if len(fecha)==10:
            print('Día', fecha[0:2])
            print('Mes', fecha[3:5])
            print('Año', fecha[6:10])
        elif (len(fecha)<10) and ("/" in fecha)==True:
            print('Día', fecha.split("/")[0])
            print('Mes', fecha.split("/")[1])
            print('Año', fecha.split("/")[2])
        else:
            print("Introduzca la fecha en el formato adecuado dd/mm/aaaa.")
            continue
        break
    except ValueError:
        print("Formato inválido.")
        input("Presione cualquier tecla para continuar ...")

#EJERCICIO REVIEW - 2 - EDGAR MAURICIO MEZA REY
#N Vendedores
def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            if num == -1:
                num=-1
                break
            elif num < 1:
                print("El numero no puede menor 1")
                input("Presione cualquier tecla para continuar ...")
                continue
            break
        except ValueError:
            print("Número inválido.")
            input("Presione cualquier tecla para continuar ...")
    return num

def leerNombre(msg):
    while True:
            try:
                nom = input(msg)
                if nom == None or nom.strip() == "":
                    print("No puede ser vacio.")
                    input("Presione cualquier tecla para continuar ...")
                    continue
                break
            except Exception as e:
                print("Nombre inválido.", e)
                input("Presione cualquier tecla para continuar ...")
            
    return nom

def tipoVenta(msg):
    while True:
            try:
                tipo = input(msg)
                if int(tipo) == 1:
                    tipo=0.2
                    break
                elif int(tipo) == 2:
                    tipo=0.15
                    break
                elif int(tipo) == 3:
                    tipo=0.25
                    break
                print("Escriba un número entre 1 a 3")
                continue
            except ValueError:
                print("Nombre inválido.")
                input("Presione cualquier tecla para continuar ...")
    return tipo 



while True:
    try:
        num = leerEntero("Cantidad de vendedores: ")
        valtot = 0
        comitot = 0
        for i in range(1, num+1):
            print("\nVendedor #", i)
            ced = leerEntero("Ingrese la cédula: ")
            if ced==-1:
                print("El programa finalizó")
                exit()
                break
            nom = leerNombre("Nombre: ")
            tipo = tipoVenta("Tipo de venta: ")
            ventaComis=0
            v=int(input(f"Cuantas ventas realizó {nom}: "))
            for i in range(1, v+1):
                print("Venta ",i)
                ventas = leerEntero("Ingrese el valor de la venta: ")
                ventaComis=ventas*tipo
            valtot += ventas
    except ValueError:
        print("Caracter inválido.")