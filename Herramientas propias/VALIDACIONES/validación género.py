def esGenero(msg):
    while True:
        try:
            n = input(msg)
            gen=n.lower()
            if gen =="f" or gen == "m":
                return gen
            else:
                print("Error, ",n, " no es un género válido m/f .")
                continue
        except ValueError:
            print("Oops!")
            continue

nom = esGenero("Ingrese género: ")
print(nom)