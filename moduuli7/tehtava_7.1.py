def print_season():
    seasons = ("talvi", "kevät", "kesä", "syksy")

    month = int(input("Anna kuukauden numero (1-12): "))

    if 1 <= month <= 12:
        season = seasons[month % 12 // 3]
        print(f"Kuukausi {month} kuuluu vuodenaikaan: {season}.")
    else:
        print("Virhe: Anna kuukausi numerona välillä 1-12.")

print_season()
