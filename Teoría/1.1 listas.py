nums=[1,2,3]
print(nums, " >> lista")

#VER
print(nums[0]," >> --nums[0]-- devuelve el valor dentro del índice de la lista")

#AGREGAR
nums.append(4)
print(nums," >> --nums.append(4)-- sumado 4")

#BORRAR
del nums[1]
print(nums," >> --del nums[1]-- eliminado 2")

#EXTENDER
nums.extend([5, 6, 7])
print(nums)

#-------------------OTROS MÉTODOS

#AGREGAR UNA LISTA A UNA LISTA
nums.append([8, 9, 10])
print(nums)

#MODIFICIAR UN ELEMENTO
nums[5] = "siete"
print(nums)

#Slice de la lista
print(nums[5:7])

lst = [2, 3, 4, 5, [60,80], "Maria"]



lst.insert(4, -3) # INSERTA EL VALOR EN LA LISTA EN LA POSICIÓN N (N, VALOR)
print(lst)


lst.pop(3) #ELIMINA EL VALOR DE LA LISTA POSICIÓN N (N)
print(lst)

lst.remove("Maria") #ELIMINA EL VALOR DE LA LISTA (N)
print(lst)

lst1 = lst.copy() #COPIA LA LISTA
lst1.pop()
print(lst)
print(lst1)

print(lst.count("Mauricio"))#CUENTA LA CANTIDAD DE VECES QUE APARECE UN ELEMENTO

print(lst.index("Mauricio"))#DEVUELVE LA PRIMERA POSICIÓN DONDE APARECE EL EMENTO