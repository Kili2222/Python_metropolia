def tuumamaara():
    while True:
        tuuma = float(input("Anna tuuma määrä: "))
        sentti = tuuma * 2.54
        if tuuma < 0:
            print("Virheellinen luku")
            break
        print(sentti)
tuumamaara()