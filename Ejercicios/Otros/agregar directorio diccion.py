# estudiantes=[
#     'id':
#         {'nombre':nom, 'notas':[nota1,nota2,nota3]}
# ]

# print(estudiantes["id"])

estudiantes={}
id = int(input("Id del estudiante: "))

nom = input("Nombre del estudiante: ")
nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
notas=[nota1,nota2,nota3]

estudiantes[id]={"nombre":nom, 'notas':notas}

print(estudiantes)
