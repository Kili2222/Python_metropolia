def main():
    sanani = ["koirat","astronautti","kivi","viha","kauppakassi","kuva","saksa","wien","puutiasaivokuume"]
    kirjaimet = 0
    for sana in sanani:
        if len(sana) > 5:
            kirjaimet = kirjaimet + 1
    print("Yli 5 kirjainta sisältäviä sanoja on:", kirjaimet)
main()