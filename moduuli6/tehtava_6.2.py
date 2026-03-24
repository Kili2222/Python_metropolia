import random

def supernoppa(tahkojenmaara):
     return(random.randint(1, tahkojenmaara))

def main():
    tahkojenmaara = int(input("Anna arpakuution sivujen lukumäärä (vähintään 1): "))
    while True:
        result = supernoppa(tahkojenmaara)
        print(f"Arvottu silmäluku on: {result}")
        if result == tahkojenmaara:
            print(tahkojenmaara, "tuli!")
            break
    return()

if __name__ == "__main__":
    main()