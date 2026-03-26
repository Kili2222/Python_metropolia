def kertaus4():
    tarina = ""
    while True:
        sana = input("Anna sana (kirjoita 'loppu' lopettaaksesi, saat kuulla tarinasi): ")
        if sana == "loppu":
            print("Muodostunut tarina:")
            print(tarina)
            break
        else:
            tarina += sana + " "
kertaus4()