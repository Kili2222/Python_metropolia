def main():
    luku=int(input("Anna luku 1-10, ohjelma tulostaa luvun kertotaulun: "))
    if luku<11:
        for i in range(1,11):
            print(f"Kertotaulu luvullesi on: {luku*i}")
    else:
        main()
main()
