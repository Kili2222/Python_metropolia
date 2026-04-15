Lentoasemat = {}

def populate_sample_data():
    sample_data = {
        "EFHK": "Helsinki-Vantaa Lentoasema",
        "KJFK": "John F. Kennedy International Airport",
        "EGLL": "London Heathrow Airport",
        "LFPG": "Charles de Gaulle Airport",
        "RJTT": "Tokyo Haneda Airport"
    }
    Lentoasemat.update(sample_data)

def add_airport():
    icao_code = input("Anna lentoaseman ICAO-koodi: ").upper()
    name = input("Anna lentoaseman nimi: ")
    Lentoasemat[icao_code] = name
    print(f"Lentoasema {name} lisätty koodilla {icao_code}.")

def search_airport():
    icao_code = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
    if icao_code in Lentoasemat:
        print(f"Lentoaseman nimi: {Lentoasemat[icao_code]}")
    else:
        print("Lentoasemaa ei löydy.")

def switch(choise):
    return {
        '1': add_airport,
        '2': search_airport,
        '3': exit
    }.get(choise, lambda: print("Virheellinen valinta, yritä uudelleen."))()

def main():
    while True:
        print("\nValitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")
        choice = input("Valintasi (1/2/3): ")
        switch(choice)
main()