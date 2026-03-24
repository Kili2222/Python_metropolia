import random
def nopanheitto():
    return (random.randint(1, 6))


def main():
    while True:
        result = nopanheitto()
        print(f"Arvottu silmäluku: {result}")
        if result == 6:
            print("Kuusi tuli!")
            break
    return ()


if __name__ == "__main__":
    main()