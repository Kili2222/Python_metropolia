def numerot():
    numerot = []
    while True:
        vastaus = input("Anna numero: ")
        if vastaus == "":
            break
        numero = int(vastaus)
        numerot.append(numero)
    print(f"Pienin numero: {min(numerot)}")
    print(f"Suurin numero: {max(numerot)}")
numerot()