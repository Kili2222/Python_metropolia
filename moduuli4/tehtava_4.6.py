import random

def lasku_pi():
    numeropisteet = int(input("Anna arvottavien pisteiden määrä: "))
    sisaympyra = 0

    for _ in range(numeropisteet):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            sisaympyra += 1

    pi_estimate = 4 * sisaympyra / numeropisteet
    print(f"Piin likiarvo on: {pi_estimate}")

def main():
    lasku_pi()

if __name__ == "__main__":
    main()