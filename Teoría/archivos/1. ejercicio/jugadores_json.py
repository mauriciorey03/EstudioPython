import json
#{ jugador : {'nom':0, 'edad':0, 'peso':0} }

import json
with open('jugadores.json') as players:
    jugador = json.load(players)

for player,num in jugador.items():
    print('Nombre: ', num['nombre'])
    print('Edad: ', num['edad'])
    print('Peso: ', num['peso'])


cont = 0
cod = True
while cod:
    
    print("\nIngrese los datos del jugador  #", cont + 1)
    pregunta=input('Desea agregar un jugador? [S]i - [N]o: \n')
    if pregunta.lower() == "n":
        cod=False
        break
    elif pregunta.lower()=="s":        
        cont += 1
        code = input ("Ingrese el código: ")
        name = input("Ingrese el nombre: ")
        age = int(input("Ingrese la edad: "))
        weight = int(input("Ingrese el peso: "))
        datos = { "nombre" : name, "edad" : age, "peso" : weight}
        
        jugador[code]=datos

print("Creando archivos")

with open('jugadores.json','w') as archivo:
    json.dump(jugador,archivo,indent=4)
