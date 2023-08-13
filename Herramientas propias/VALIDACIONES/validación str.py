def esStr(msg):
    while True:
        try:
            n = input(msg)
            if n == None or n.strip() == "":
                print("Error campo vacío inválido.")
                continue
            elif n.isnumeric:
                print("Error", n, "es un número. Ingrese letras.")
                continue
            return n
        except ValueError:
            print("Oops!")
            continue

nom = esStr("Ingrese str: ")