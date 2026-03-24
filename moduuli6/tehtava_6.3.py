gallona = 3.785

def gallonat_litroiksi(gallons):
    litrat = gallons * gallona
    return litrat

def main():
    while True:
        gallons = input("Anna bensiinin määrä gallonina: ")
        try:
            gallons = float(gallons)
        except ValueError:
            print("Virhe: Syötä kelvollinen luku.")
            continue
        if gallons < 0:
            print("Negatiivinen luku syötetty, ohjelma lopetetaan.")
            break
        litrat = gallonat_litroiksi(gallons)
        print(f"{gallons} gallonaa on {litrat:.3f} litraa.")
    return
main()