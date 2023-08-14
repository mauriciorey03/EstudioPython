# archivo=input("Ingrese el nombre")
nombre=("Datos.txt")

archivoLectura= open(nombre, "r+")

unaLinea=archivoLectura.readline()

archivoEscritura=open("Destino.txt","w")
archivoEscritura.write(linea)
archivoEscritura.close()



print("Fin")
