# usuario = [ {cod, nom, nota}, {cod, nom, nota}  ]

# usuario = {
#     cod1 : [nom, n1, n2, n3, nd, a/r],
#     cod2 : [nom, n1, n2, n3, nd, a/r],
# }

# usuario = {
#     cod1 : {'nom':0, 'n1':0, 'n2':0,'n3':0,'nd':0, 'resultado':a/r}
# }

usuario = []
cont = 0
cod = 0
while cod != 999:
    print("\nDatos  #", cont + 1)
    cod = int(input("Codigo: "))
    if cod != 999:
        cont += 1
        datos = { "codigo" : cod }
        datos["nom"] = input("Nombre: ")
        datos["nota1"] = int((input("Ingrese el valor 1 ")))
        datos["nota2"] = int((input("Ingrese el valor 2 ")))
        datos["nota3"] = int((input("Ingrese el valor 3 ")))
        
        usuario.append(datos)
        
print("\n","=" * 40)
print("\tINFORME DE DATOS")
print("=" * 40)

print(usuario)

for elem in usuario:
    print(f"{elem['nom']}")
    
# for i in range(len(usuario)):
#     print(f"{usuario[i]['nom']}\t{usuario[i]['notadef']}\t{usuario[i]['estado']}")