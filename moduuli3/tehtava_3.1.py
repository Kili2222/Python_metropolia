def kalanmitta():
    kuhanpituus = float(input("Kerro kuhan mitta senttimetreinä: "))
    if kuhanpituus <= 0:
        print("Tuo ei ole pituus kuhalle")
    elif kuhanpituus < 37:
        print(f"Kuha on {37-kuhanpituus}senttimetriä liian pieni, laske kala takaisin järveen.")
    else:
        print("Hieno kala <3")
kalanmitta()
