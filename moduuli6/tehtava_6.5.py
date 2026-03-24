def poistaparittomat(numerot):
    parilliset = []
    for numero in numerot:
        if numero % 2 == 0:
            parilliset.append(numero)
    return parilliset

def main():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = poistaparittomat(test_list)
    print(f"Alkuperäinen lista: {test_list}")
    print(f"Karsittu lista (vain parilliset luvut): {filtered_list}")
    return
main()