def hyttipaikka():
    hyttiluokka = input("Kerro hyttiluokkasi, kiitos: ").upper()
    if hyttiluokka == "LUX":
        print("Lux on parveekkeelinen hytti yläkannella")
    elif hyttiluokka == "A":
        print("A on ikkunallinen hytti autokkanen yläpuolella")
    elif hyttiluokka == "B":
        print("B on ikkunaton hytti autokannen yläpuolella")
    elif hyttiluokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella")
    else:
        print("Virheellinen hyttiluokka")
        hyttipaikka()
hyttipaikka()