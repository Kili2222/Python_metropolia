def workhours():
    tunnit = float(input("Anna tekemäsi tunnit: "))
    workday=input("Anna viikonpäivä: ")
    tuntipalkka=float(input("Anna tuntipalkka: "))
    if "sunnuntai" != workday:
        palkka=tunnit*tuntipalkka
        print("Palkkasi on", palkka)
    else:
        supalkka=(tuntipalkka*2)*tunnit
        print("Palkkasi on", supalkka)
workhours()
