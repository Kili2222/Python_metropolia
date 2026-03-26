def kertaus3():
    import math

    while True:
        luku = int(input("Anna kokonaisluku (numero 0 lopettaa ohjelman): "))

        if luku == 0:
            print("Ohjelma lopetetaan!.")
            break
        elif luku < 0:
            print("Virheellinen numero")
        else:
            juuri = math.sqrt(luku)
            print(f"Luvun neliöjuuri on {juuri}")
kertaus3()