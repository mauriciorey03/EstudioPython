clientes='pablo,ricardo,'


def crea_cliente(cliente_nombre):
    global clientes

    if cliente_nombre not in clientes:
        clientes+=cliente_nombre
        add_comma()
    else:
        print('El cliente ya está en la lista de clientes.')

def lista_clientes():
    global clientes
    print(clientes)

def add_comma():
    global clientes

    clientes+= ','


def escribir_bienvenida():
    print("Bienvenido al software de ventas")
    print('*'*50)
    print('Qué te gustaría hacer?')
    print('[A]gregar cliente')
    print('[E]liminar cliente')


if __name__ == '__main__':
    escribir_bienvenida()
    comando = input().upper()
    if comando == 'A':
        cliente_nombre=input('Nombre del cliente: ')
        crea_cliente(cliente_nombre)
        lista_clientes()
    elif comando == 'E':
        pass
    else:
        print('Comando inválido.')