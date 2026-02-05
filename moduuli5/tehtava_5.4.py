def city():
    kaupungit = []
    for i in range (5):
        kaupunki = input("Anna kaupungin nimi: ")
        kaupungit.append(kaupunki)
    print("Kirjoittamasi kaupungit")
    for kaupunki in kaupungit:
        print(kaupunki)
city()
