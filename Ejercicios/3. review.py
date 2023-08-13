# EJERCIO - 1 - EDGAR MAURICIO MEZA REY
for i in range (1,1000):
    if ((i % 3 == 0) or (i % 7 == 0)):
        print(i)

#EJERCICIO - 2 - EDGAR MAURICIO MEZA REY
n=int(input("Ingrese un número "))
n=n
print("1","-",end="")
for i in range(1,n):
    sig=((-1)**(i+1))
    imp=str(1/i)
    if (sig==1):
        print(f"1/{i+1}","+",end="")
    else:
        print(f"1/{i+1}","-",end="")

p=int(input("Ingrese el número 1: "))
q=int(input("Ingrese el número 2: "))

#EJERCICIO - 3 - EDGAR MAURICIO MEZA REY
suma1=0
formula=((p**3)+(q**4))-(2*(p**2))
for i in range(0,681):
    if formula < 680:
        suma1=suma1+i

print(f"{suma1:,.0f}")

#EJERCICIO - 4 - EDGAR MAURICIO MEZA REY
contador=0
mayor=0
menor=0
for i in range(0,10):
    n=int(input("Ingrese un número "))
    num=n
    
    contador=contador+1
    if n>mayor:
        mayor=n
    if n<mayor:
        menor=n
print(f"El número mayor es: {mayor}.")
print(f"El número menor es: {menor}.")

#EJERCICIO - 5 - EDGAR MAURICIO MEZA REY
c=2
a=1
b=1

print("Hallar la secuencia de 1, 1, 2, -1...")
print("El patrón es de el T(n)+((-1)^(n+1)*t(n+1))=T(n+2)\n")
print(f"Primeros números: \n1 \n1")
for n in range (1,20):
    c=c
    a=a
    b=b
    sig=((-1)**(n+1))
    if (sig==1):
        c=a+(b)
#validación
#        print(f"valor {a}+{b}={c}")
        print(c)
        a=c
    else:
        d=b-c
#validación        
#        print(f"valor {b}-{c}={d}")
        print(d)
        a=c
        b=d
#EJERCIO - 6 - EDGAR MAURICIO MEZA REY

contador=0
promedio=0
estaBRUTO=0
estaEPS=0
estaPEN=0
estaNETO=0
mayor=0
menor=0
empleadoMay=0
empleadoMen=0
print("Bienvenido al liquidador de la empresa ACME \ndesea calcular el salario de cuantos empleados?: ")

n=int(input("Ingrese un número "))
n=n
for i in range (1,n+1):
    print("Empleado, ",i)
    hor=int(input("Ingrese el total de horas de trabajo: "))
    name=0
    name=input("Ingrese el nombre: ")
    
    valHor=float(20000)
    sueBru=int(valHor*hor)
    desEps=int(sueBru*0.04)
    desPen=int(sueBru*0.04)
    desNetEps=int(sueBru-desEps)
    desNetPen=int(sueBru-desPen)
    sueNet=int(sueBru-(desPen+desEps))

    print("\n","-"*20)
    print("Liquidación del sueldo del trabajador: ", i, name)
    print(f"Total de horas trabajadas: {hor}")
    print(f"Sueldo bruto: ${sueBru:,.0f}")
    print(f"Descuento EPS: ${desEps:,.0f}")
    print(f"Descuento Pensión: ${desPen:,.0f}")
    print(f"Total de salario neto: ${sueNet:,.0f}")
    print("\n","-"*20)
    estaBRUTO=sueBru+estaBRUTO
    estaNETO=sueNet+estaNETO
    estaEPS=desEps+estaEPS
    estaPEN=desPen+estaPEN
    promedioBruto=estaBRUTO/i
    PromedioNETO=estaNETO/i
    PromedioEPS=estaEPS/i
    PromedioPEN=estaPEN/i

    n=sueNet
    if n>mayor:
        mayor=n
        empleadoMay=i
        nomMay=name
    if n<mayor:
        menor=n
        empleadoMen=i
        nomMen=name

print("\n","-"*20)
print(f"Total de salario bruto: {estaBRUTO:,.0f}")
print(f"Total de aportes eps: {estaEPS:,.0f}")
print(f"Total de aportes pensión: {estaPEN:,.0f}")
print(f"Total de salario neto: {estaNETO:,.0f}")
print("-"*20)
print(f"El mayor salario neto de {nomMay} es: {mayor:,.0f}.")
print(f"El menor salario neto de {nomMen} es: {menor:,.0f}.")
print("-"*20)
print(f"Promedio salario bruto: {promedioBruto:,.0f}")
print(f"Promedio salario neto: {PromedioNETO:,.0f}")
print(f"Promedio eps: {PromedioEPS:,.0f}")
print(f"Promedio pensión: {PromedioPEN:,.0f}")
print("-"*20)

print("Validador de números amigos.")
print("-"*20)
n1=int(input("Ingrese el número 1: "))
n2=int(input("Ingrese el número 2: "))

#EJERCIO - 7 - EDGAR MAURICIO MEZA REY
n1=print("Escribe n1: ")
n2=print("Escribi n2: ")
suma1=0
suma2=0
for i in range(1,n1+1):
    if n1 % i == 0:
        suma1=suma1+i
for i in range(1,n2+1):
    if n2 % i == 0:
        suma2=suma2+i

if suma1 == suma2:
    print("Son amigos")
else:
    print("No son amigos")