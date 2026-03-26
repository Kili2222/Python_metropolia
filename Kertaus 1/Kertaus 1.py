def kertaus1():

    nimi = input("Kerro nimesi: ")

    if nimi != "Matti":
        keittoa = int(input("Kuinka monta keittoannosta haluat? "))
        hinta = keittoa * 5.90
        print(f"Kokonaishinta on {hinta:.2f} euroa.")
        print("Seuraava kiitos")
    else:
        print("Seuraava kiitos")

kertaus1()