def suurin_numero(a,b,c):
    return max(a,b,c)
luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))
suurin = suurin_numero(luku1,luku2,luku3)
print("Suurin numero on:", suurin)
