def lasku():
    kokonaisluku1=(int(input("Anna ensimmäinen kokonaisluku: ")))
    kokonaisluku2 = (int(input("Anna toinen kokonaisluku: ")))
    kokonaisluku3 = (int(input("Anna kolmas kokonaisluku: ")))
    summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
    tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
    keskiarvo = summa /3
    print(summa)
    print(tulo)
    print(keskiarvo)
lasku()