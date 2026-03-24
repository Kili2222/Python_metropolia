import math

def pizza_kplhinta(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    hintakpl = price_eur / area_m2
    return hintakpl

def main():
    kplhinnat = []
    for i in range(2):
        print(f"Pizza {i+1}:")
        diameter = float(input("Anna pizzan halkaisija senttimetreinä: "))
        hinta = float(input("Anna pizzan hinta euroina: "))
        unit_price = pizza_kplhinta(diameter, hinta)
        kplhinnat.append(unit_price)
        print(f"Pizzan {i+1} yksikköhinta: {kplhinnat[i]:.2f} €/m²\n")

    if kplhinnat[0] < kplhinnat[1]:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif kplhinnat[1] < kplhinnat[0]:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmilla pizzoilla on sama yksikköhinta.")
main()