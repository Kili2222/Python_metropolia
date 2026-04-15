def nimienkeraus():
    names = set()

    while True:
        name = input("Syötä nimi (tai paina Enter lopettaaksesi): ")
        if name == "":
            break
        if name in names:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            names.add(name)

    print("Syötetyt nimet:")
    for name in names:
        print(name)
nimienkeraus()