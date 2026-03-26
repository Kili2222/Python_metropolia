def kertaus2():
    tuntipalkka = float(input("Anna tuntipalkka: "))
    tunnit = float(input("Anna tehdyt tunnit: "))
    paiva = input("Anna viikonpäivä: ")

    if paiva.lower() == "sunnuntai":
        paivapalkka = tuntipalkka * 2 * tunnit
    else:
        paivapalkka = tuntipalkka * tunnit
        print(f"Päiväpalkka on {paivapalkka:.2f} euroa.")
kertaus2()