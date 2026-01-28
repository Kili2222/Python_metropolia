def kirjautuminen():
    tunnus = "python"
    salasana = "rules"
    kerrat = 0
    while kerrat < 5:
        kysytunnus = input("Kirjoita käyttäjätunnuksesi: ")
        kysysalasana = input("Kirjoita salasana: ")
        if kysytunnus == tunnus and kysysalasana == salasana:
            print("Tervetuloa!!")
            break
        else:
            print("Väärin, yritä uudelleen")
        kerrat += 1
    if kerrat == 5:
        print("Pääsy evätty")
kirjautuminen()