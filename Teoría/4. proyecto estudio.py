import sys
clients = 'pablo,ricardo,'


def create_client(client_name): #crea el cliente
    global clients

    if client_name not in clients:
        clients+= client_name
        add_comma() 
    else:
        print('El cliente ya está en la lista de clientes.')


def list_clients(): #muestra la lista de clientes
    global clients
    print(clients)


def update_client(client_name, updated_client_name): # modifica el cliente, con el segundo parametro update_client
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print("Client's not in clients list.")

def add_comma(): 
    global clients

    clients+= ','


def delete_client(): #elimina el cliente reemplazandolo por espacio vacío
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print("Client's not in clients list.")

def search_client(client_name):
    clients_list=clients.split(",")
    for client in clients_list: #Busca la coincidencia entre los clientes
        if client != client_name:
            continue
        else:
            return True


def print_welcome():
    print("Bienvenido al software de ventas")
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
    print_welcome()

    comando = input().upper()

    if comando == 'C':
        client_name=get_client_name()
        create_client(client_name)
        list_clients()
    elif comando == 'R':
        list_clients()
    elif  comando == 'U': # actualiza, con el valor del cliente original y el posterior en los argumentos
        client_name = get_client_name()
        updated_client_name = input ("What's the updated client name?")
        update_client(client_name,updated_client_name)
        list_clients()
    elif comando == 'D':
        client_name = get_client_name()
        delete_client() # pregunta y elimina al cliente
        list_clients() # muestra la lista
        delete_client() # demuestra el valor actualizado
    elif comando == 'S':
        client_name = get_client_name()
        found = search_client(client_name)
        if found:
            print("The client is in the client's list")
        else:
            print("The client: {} isn't in the client's list".format(client_name)) #El format es reemplazado por el client_name
    else:
        print('Comando inválido.')
