def listasumma(numbers):
    summa = 0
    for numero in numbers:
        summa += numero
    return summa

def main():
    test_list = [3, 5, 7, 2, 8]
    tulos = listasumma(test_list)
    print(f"Listan {test_list} lukujen summa on: {tulos}")
    return
main()