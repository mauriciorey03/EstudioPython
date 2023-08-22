lista_numeros = list(range(100))
#print(lista_numeros)

#estructura
# [elem for elem in list if element meets condition]
pares = [num for num in lista_numeros if num % 2 == 0 ]
#print(pares)

students_uid = [1,2,3]
students = ['Juan', 'Jose', 'Larsen']

#JUNTA DOS LISTAS EN DICCIONARIOS
students_with_uid = {uid: student for uid, student in zip(students_uid, students)}
print(students_with_uid)

noms_nums=[1,2,3,4,5,6]
noms=['a','b','c','d','e']

nueva = {name: nums for name, nums in zip(noms, noms_nums)}
print(nueva)


#ejercicio que borra los números repetidos:
import random
numeros_random = []
for i in range(10):
    numeros_random.append(random.randint(1,3))
sin_repetir = {numeros for numeros in numeros_random}
print(sin_repetir)
