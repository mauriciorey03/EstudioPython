# #N Vendedores
# n=int(input("Cuantos vendedores voy a revisar: "))
# for i in range (1,n+1):
while True:
    try:
        idVende=int(input("Ingrese documento de identidad: "))
        if idVende < 0:
            continue
        break
    except ValueError:
        print("Ha sucedido un Error, ingrese un número de documento.")
while True:
    try:
        nombreVende=input("Nombre del vendedor: ")
        if nombreVende== None or nombreVende.strip()=="":
            print("Nombre inválido por favor ingrese una letra")
            continue
        break
    except ValueError:
        print("Ha sucedido un Error, ingrese un nombre válido.")
while True:
    try:
        tipoVendedor=int(input("Ingrese el tipo de vendedor: 1=Puerta a puerta, 2=Telemercadeo, 3=Ejecutivo de ventas "))
        if (tipoVendedor<1 or tipoVendedor>3):
            print("Ingrese un número entre 1, 2 o 3")
            continue
        break  
    except ValueError:
        print("Ha sucedido un error, ingrese un número entre 1, 2 o 3")
if tipoVendedor == 1:
    contado=0.25
    credito=0.20
elif tipoVendedor == 2:
    contado=0.15
    credito=10
elif tipoVendedor== 3:
    contado=0.20
    credito=0.15
print("Ahora incluiremos el los datos del cliente ", idVende, nombreVende, tipoVendedor, contado, credito)

while True:
    try:
        nameCompra=input("Nombre del comprador: ")
        if nameCompra== None or nameCompra.strip()=="":
            print("Nombre inválido, por favor ingrese una nombre.")
            continue
        break
    except ValueError:
        print("Ha sucedido un Error, ingrese un nombre válido.")

while True:
    try:
        idCompra=int(input("Ingrese código del cliente: "))
        if idCompra < 0:
            continue
        break
    except ValueError:
        print("Ha sucedido un Error, ingres un código válido.")


while True:
    try:
        tipoVenta=int(input("Ingrese el tipo de venta: 1=Contado, 2=Credito "))
        if (tipoVenta<1 or tipoVenta>2):
            print("Ingrese el tipo de venta 1=Contado, 2=Credito")
            continue
        break  
    except ValueError:
        print("Ha sucedido un error, ingrese un número entre 1 o 2")

while True:
    try:
        valorVenta=int(input("Ingrese valor de venta válido: "))
        if idCompra < 0:
            continue
        break
    except ValueError:
        print("Ha sucedido un Error, ingres un código Ingrese valor de venta válido:")

if tipoVenta == 1:
    tipoComi=contado
elif tipoVenta == 2:
    tipoComi=credito

print(f"La comisión por venta de {idVende} nombre {nombreVende}, por la compra de {nameCompra} es de {tipoComi*valorVenta}")

# nombreCliente=input("Ingrese nombre del cliente: ")
# codCliente=input("Ingrese cliente: ")
# valorVenta=input("Valor de la venta")
