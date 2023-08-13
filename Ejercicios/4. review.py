#EJERCIO 1 -EDGAR MAURICIO MEZA REY
n1=int(input("Escribe n1: "))
n2=int(input("Escribi n2: "))
suma1=0
suma2=0

while n1 < 7:
    print(n1)
    n1 = suma1+1
    break
print (suma1)

#EJERCIO 2 -EDGAR MAURICIO MEZA REY


n = int(input("Escriba un número : "))

for i in range(2, n):
    if n % i == 0:
            primo=True
    else:
        primo=False
print(n, primo)

if primo==True:
    print("Es primo")
else:
    print("No es primo")

while (n >=0):
    print(f"El número {n} es {primo}")
    n = int(input("Escriba un número : "))

print("El número es negativo.")

#EJERCIO 3 -EDGAR MAURICIO MEZA REY
num = float(input("Escriba un número mayor que 0: "))

while num > 0:
    num = int(input(f"{num} es mayor que cero. Escriba otro número mayor que 0: "))
    print()

print(f"El número {num} no es menor que cero.")

#EJERCIO 4 -EDGAR MAURICIO MEZA REY

n = int(input("Escriba un número entre 0 y 5 o FIN para terminar: "))
suma=0
i=1

while (i <= n):
        print(f"La nota número, ",i)
        nota=input("Ingrese la siguiente nota: ")
        if nota=="FIN" or nota=="fin":
                break
        suma=suma+float(nota)
        i+=1
prom=suma/(i-1)

print(f"El promedio de nota es de {prom}.")