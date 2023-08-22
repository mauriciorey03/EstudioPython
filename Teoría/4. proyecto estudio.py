import sys
import csv
import os
CLIENTS_TABLE = '.clients.csv'
CLIENTS_SCHEMA = ['nombre','company','email','position']
clients = []


def initialize_clients_from_storage():
    with open(CLIENTS_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=[CLIENTS_SCHEMA])
        for row in reader:
            clients.append(row)

def save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENTS_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer= csv.DictWriter(f, fieldnames=CLIENTS_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENTS_TABLE)
    os.rename(tmp_table_name, CLIENTS_TABLE)



def create_client(client): #crea el cliente
    global clients #global permite extender el alcance

    if client not in clients: #si... el nombre no está en la lista
        clients.append(client) #agrega el nombre
    else:
        print('The client is alredy in the list.') #si ya está, print este mensaje

def get_client_from_user():
    client= {
        'name':get_client_field('name'),
        'company':get_client_field('company'),
        'email': get_client_field('email'),
        'position': get_client_field('position')
    }
    return client

def get_client_field(field_name): #construir esta función
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field

def list_clients(): #Función que muestra la lista de clientes
    for indice, client in enumerate(clients):# esta FUNCIÓN permite ciclar y enumerar el índice ÚTIL pendiente ver más documentación
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = indice,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))
        #print('{}: {}'.format(indice, client['name'])) #client es una var autonóma, propia para esta función


def update_client(client_id, updated_name): # modifica el cliente, con el segundo parametro update_client
    global clients

    if len() -1 >= client_id:
        client[client_id] = updated_name
    #RECORRIDO EN LISTA
    #if client_name in clients:
        #clients = clients.replace(client_name + ',', updated_name + ',') #de esta forma es mediante reemplazo
        # index = clients.index(client_name) #esta FUNCIÓN devuelve la posición del elemento según su índice
        # clients[index] = updated_name #Reemplaza el nombre que buscó, por uno nuevo
    else:
        print("Client's not in clients list.")


def delete_client(client_id): #elimina el cliente reemplazandolo por espacio vacío
    global clients
    
    for indice, client in enumerate(client):
            if indice == client_id:
                del client[indice]
                break
    #if client_name in clients:
        #clients.remove(client_name)
        #clients = clients.replace(client_name + ',', '')
    else:
        print("Client's not in clients list.")


def search_client(client_name):
    #clients_list=clients.split(",")
    for client in clients: #Busca la coincidencia entre la lista de los clientes
        if client['name'] != client_name: #itera dentro de la lista y si es igual, devuelve el valor
            continue
        else:
            return True





def print_welcome():#bienvenida del usuario
    print("Welcome to the software POS Mauro")
    print('*'*50)
    print('What would like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]eleate client')
    print('[S]earch client')




def get_client_name(): #pregunta por el nombre del cliente, hasta que lo ingrese
    client_name = None
    while not client_name:
        client_name = input("What's the client name?")

        if client_name == 'exit':
            client_name = None
            break

        if not client_name:
            sys.exit() #Termina el programa con la libreria de sys
    
    return client_name


if __name__ == '__main__':
    initialize_clients_from_storage()
    print_welcome()

    comando = input().upper()

    if comando == 'C':
        client = get_client_from_user()
        create_client(client)
        list_clients()
    elif comando == 'R':
        list_clients()
    elif  comando == 'U': # actualiza, con el valor del cliente original y el posterior en los argumentos
        client_id = int(get_client_field('id'))
        updated_name = get_client_from_user()
        update_client(client_id,updated_name)
        list_clients()
    elif comando == 'D':
        client_id = int(get_client_field('id'))
        client_name = get_client_name()
        delete_client() # pregunta y elimina al cliente
        list_clients() # muestra la lista
        delete_client() # demuestra el valor actualizado
    elif comando == 'S':
        client_name = get_client_name()
        found = search_client(client_name)
        if found:
            print("The client {} is in the client's list".format(client_name))
        else:
            print("The client: {} isn't in our client's list".format(client_name)) #El format es reemplazado por el client_name
    else:
        print('Comando inválido.')


save_clients_to_storage()