def hemoarvot():
    sukupuoli = input("Oletko biologiselta sukupuoleltasi mies vai nainen?: ").lower()
    if sukupuoli == "mies":
        hemoglobin = int(input("Kerro hemoglobiini arvosi: "))
        if hemoglobin < 134:
            print("Hemoglobiinisi on liian alhainen")
        elif 134 <= hemoglobin <= 195:
            print("Hemoglobiinisi on normaali")
        elif hemoglobin > 195:
            print("Hemoglobiinisi on liian korkea")
    elif sukupuoli == "nainen":
        hemoglobin = input("Kerro hemoglobiini arvosi: ")
        if hemoglobin < 117:
            print("Hemoglobiinisi on liian alhainen")
        elif 117 <= hemoglobin <= 175:
            print("Hemoglobiinisi on normaali")
        elif hemoglobin > 175:
            print("Hemoglobiinisi on liian korkea")
    else:
        hemoarvot()
hemoarvot()