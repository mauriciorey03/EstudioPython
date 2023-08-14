
# estudiantes = { cod1: {
#             nombre:"",
#             nota 1:"",
#             nota2:"",
#             nota3;"",
#             resultado: Aprueba/Reprueba
#         },
#               cod2: {
#             nombre:"",
#             nota 1:"",
#             nota2:"",
#             nota3;"",
#             resultado: Aprueba/Reprueba
#         },

def evaluacion(a,b,c):
    val1=int(a*0.3)
    val2=int(b*0.3)
    val3=int(c*0.4)
    resultado=val1+val2+val3
    if resultado >= 3:
        evalua="Aprueba"
    elif resultado< 3:
        evalua="Reprueba"
    return evalua, resultado



doc = {}
num=0
while True:
        num+=1
        print("\nDatos del estudiante #",num)
        id =int(input("Código del estudiante: "))
        if id == 999:
            break
        nom = input("Nombre? ")
        Nota1 = int(input("Ingrese la primera nota: "))
        Nota2 = int(input("Ingrese la segunda nota: "))
        Nota3 = int(input("Ingrese la tercera nota: "))
        aprueba, definitiva = evaluacion(Nota1,Nota2,Nota3)
        Resultado=aprueba

        datos={
            "nombre": nom,
            "nota 1": Nota1,
            "nota 2": Nota2,
            "nota 3": Nota3,
            "Total": definitiva,
            "Condición": Resultado
        }
        doc[id] = datos

print()
for k, v in doc.items():
    print("El estudiante ", v["nombre"],  v['Condición'])

