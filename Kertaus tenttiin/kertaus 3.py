from math import sqrt

def laskut():
    luku=float(input("Anna luku, ohjelma tulostaa luvun neliöjuuren, 0 lopettaa ohjelman: "))
    while luku != 0 :
        if luku > 0 :
            print(sqrt(luku))
        else:
            print("Virheellinen numero")
        luku = float(input("Anna luku, ohjelma tulostaa luvun neliöjuuren, 0 lopettaa ohjelman: "))
        
    print("Ohjelma lopetetaan")
laskut()