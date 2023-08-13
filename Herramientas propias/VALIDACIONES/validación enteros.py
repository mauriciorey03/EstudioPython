def esNumero(msg):
    while True:
        try:
            n = input(msg)
            if int(n) < 1: #INT-FLOAT
                print("Error. El número debe ser mayor que 0")
                continue
            return n
        except ValueError:
            print("Oops!", n, "no es un número válido")
            continue

id = esNumero("Id del empleado: ")