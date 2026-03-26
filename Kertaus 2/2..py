luvut = []

while True:
    arvo = int(input("Uusi arvo: "))

    if arvo == 0:
        print("Hei hei!")
        break

    luvut.append(arvo)

    print(f"Lista nyt; {luvut}")
    print(f"Lista järjestyksessä: {sorted(luvut)}")