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


def print_welcome():
    print("Bienvenido al software de ventas")
    print('*'*50)
    print('What would like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]eleate client')


def get_client_name():
    return input("What's the client name?")


if __name__ == '__main__':
    print_welcome()

    comando = input().upper()

    if comando == 'C':
        client_name=get_client_name()
        create_client(client_name)
        list_clients()
    elif comando == 'D':
        client_name = get_client_name()
        pass
    elif  comando == 'U':
        client_name = get_client_name()
        updated_client_name = input ("What's the updated client name?")
        update_client(client_name,updated_client_name)
        list_clients()
    else:
        print('Comando inválido.')