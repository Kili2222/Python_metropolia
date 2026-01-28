import random
def peli():
    numero = random.randint(1,10)
    while True:
        arvaus = int(input("Arvaa numero väliltä 1-10: "))
        if arvaus == numero:
            print("Oikein!!!")
            break
        elif arvaus < numero:
            print("Numero on liian pieni, kokeile uudelleen")
        else:
            print("Numero on liian iso, kokeile uudelleen")
peli()