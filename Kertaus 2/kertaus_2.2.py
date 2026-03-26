def main():
    lista = []
    while True:
        luku = int(input("Anna luku, 0 lopettaa ohjelman: "))
        if luku == 0:
            print("Ohjelma lopetetaan")
            break
        lista.append(luku)
        print("Luvut antamassasi järjestyksessä:", lista)
        print("luvut järjestettynä pienimmästä isoimpaan:",sorted(lista))
main()
