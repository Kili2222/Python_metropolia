def keittokauppa():
    nimi = input("Kerro nimesi: ")
    if nimi != "Matti":
        keittoannos = 5.90
        maara=float(input("Montako keittoannosta? "))
        print("kokonaishinta on:", maara * keittoannos)
        print("Seuraava kiitos!")
    else :
        print("Seuraava kiitos")
keittokauppa()