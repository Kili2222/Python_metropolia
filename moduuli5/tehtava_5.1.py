import random
def arpa():
    lukumaara = int(input("Kuinka monta arpakuutiota heitetään? "))

    summa = 0

    for i in range(lukumaara):
        silmaluku = random.randint(1, 6)
        summa += silmaluku
    print("Silmälukujen summa on:", summa)
arpa()
