#INTRODUCCIÓN
#Resuelva los siguientes enunciados en Python validando la entrada del usuario y usando diccionarios.

#ENUNCIADO
#Se realiza la compra de N artículos, en donde se ingresa el codigo del artículo 
# y la cantidad y mediante el uso de diccionarios para los nombres 
# y valores unitarios de los artículos, 
# el programa debe obtener el nombre de cada artículo, 
# cantidad comprada, 
# valor unitario, 
# valor total de acuerdo con la cantidad comprada y
#finalmente calcular el valor total de la compra.

#Se suministra el diccionario de nombres de artículo y otro con los valores unitarios.
#articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
#valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

# cant = { art1: {
#             nombre:"",
#             valorUnitario: 0,
#             cantidadComprada: 0,
#             valorTotal: 0,
#         },
#
#         ced2: {
#             nombre:"",
#             valorUnitario: 0,
#             cantidadComprada: 0,
#             valorTotal: 0,
#         }
#        }

def leerEntero(msg):
    while True:
        try:
            n = int(input(f"{msg}? "))
            if n <= 0:
                print(f"{msg} no puede ser negativo ni cero")
                continue
            return n
        except ValueError:
            print(f"Error. {msg} debe ser un entero.")



def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

std = {}
valorTotal=0

cant=leerEntero("Cantidad de artículos a comprar: ")
articulos = {1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores = {1:2500,2:3800,3:1200,4:35000,5:3700}

for i in range(1, cant+1):
    print("\nDatos de la compra #",i)
    art=leerEntero("Código de artículo: 1 Lapiz, 2 Cuadernos, 3 Borrador, 4 Calculadora, 5 Escuadra")
    cant=leerEntero("Cantidad de artículos a comprar: ")
    valorArt=valores[art]*cant
    datos = {
        "Artículo": articulos[art],
        "Valor unitario": valores[art],
        "Cantidad comprada": cant,
        "Valor total": valorArt,
    }
    valorTotal+=valorArt
    std[i]=datos

print("{:^10} | {:^15} | {:^15}".format("ELEMENTO","VALOR UNIDAD","VALOR TOTAL"))

for i,k in std.items():
    #print(f"{k['Artículo']:^10} | {k['Valor unitario']:^15} | {k['Valor total']:^15}")
    print("{:^10} | {:^15} | {:^15}".format(f"{k['Artículo']}",f"{k['Valor unitario']:,.0f}",f"{k['Valor total']:,.0f}"))
    
print("VALOR FINAL $ {:,.0f}".format(valorTotal))