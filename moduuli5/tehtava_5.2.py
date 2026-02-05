def kysely():
    luvut = []
    while True:
        numero = input("Anna luku (tyhjä lopettaa): ")

        if numero == "":
            break

        luvut.append(float(numero))

    luvut.sort(reverse=True)

    print("Viisi suurinta lukua:")
    for luku in luvut[:5]:
        print(luku)
kysely()