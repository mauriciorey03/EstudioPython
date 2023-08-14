#directorio{valor:{valor:llave,valor:lista}}
# usuario={
#     'id':
#         {'nombre':nom, 'notas':[nota1,nota2,]}
# }
# usu = {}
# num=0
# while True:
#         num+=1
#         print("\nDatos #",num)
#         id =int(input("Código del estudiante: "))
#         if id == 999:
#             break
#         nom = input("Nombre? ")
#         Nota1 = int(input("Ingrese la primera nota: "))
#         Nota2 = int(input("Ingrese la segunda nota: "))
#         datos={"nombre": nom,"notas":[Nota1,Nota2]}
#         usu[id] = datos

# print()
# for cod, subvalor in usu.items():
#     print("El usuario ", cod, subvalor["nombre"],  subvalor['notas'])

# archivo=input("Ingrese el nombre")
#archivoLectura= open(archivo, "r+")

print("Escribiendo...")
archivo=open("base.txt","w")
archivo.write(input(""))
archivo.write('\n')
archivo.close()


print("Agregando...")
archivo=open("base.txt","a")
archivo.write(input(""))
archivo.write('\n')
archivo.close()

print("Leyendo...")
archivo=open("base.txt","r")
print(archivo.read())
archivo.close()


print("Fin")