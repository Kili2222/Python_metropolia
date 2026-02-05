def kysely():
    numero = int(input("Anna numero: "))
    if numero == 0 or numero == 1:
        print("Numero ei ole alkuluku")
    elif numero >1:
        for i in range(2,numero):
            if numero % i == 0:
                print(numero, "Numero ei ole alkuluku")
                break
        else:
            print("Numero on alkuluku")
    else:
        print(numero, "Numero ei ole alkuluku")
kysely()
