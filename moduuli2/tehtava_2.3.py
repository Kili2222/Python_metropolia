def lasku_piiri_ja_pintaala():
    kanta=float(input("Anna kanta: "))
    korkeus=float(input("Anna korkeus: "))
    pintaala=kanta*korkeus
    piiri=(kanta+korkeus)*2
    print(f"pintaala = {pintaala:.2f}")
    print(f"piiri = {piiri:.2f}")
lasku_piiri_ja_pintaala()