clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients+= client_name
        add_comma()
    else:
        print('El cliente ya está en la lista de clientes.')


def list_clients():
    global clients
    print(clients)


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print("Client's not in clients list.")

def add_comma():
    global clients

    clients+= ','


def delete_client():
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print("Client's not in clients list.")

def search_client()


def print_welcome():
    print("Bienvenido al software de ventas")
    print('*'*50)
    print('What would like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]eleate client')
    print('[S]earch client')


def get_client_name():
    return input("What's the client name?")


if __name__ == '__main__':
    print_welcome()

    comando = input().upper()

    if comando == 'C':
        client_name=get_client_name()
        create_client(client_name)
        list_clients()
    elif comando == 'R':
        list_clients()
    elif  comando == 'U':
        client_name = get_client_name()
        updated_client_name = input ("What's the updated client name?")
        update_client(client_name,updated_client_name)
        list_clients()
    elif comando == 'D':
        client_name = get_client_name()
        delete_client()
        list_clients()
        delete_client()
    elif comando == 'S':
        client_name = get_client_name()
        found = search_client(client_name)
    else:
        print('Comando inválido.')


        if found:
            print("The client is in the client's list")
        else:
            print("The client: {} isn't in the client's list".format(client_name))