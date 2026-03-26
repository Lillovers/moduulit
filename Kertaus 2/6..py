def summa(a, b):
    return a + b


def erotus(a, b):
    return a - b


def tulo(a, b):
    return a * b


def osamaara(a, b):
    if b == 0:
        return "Virhe: Nollalla ei voi jakaa!"
    return a / b

print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:")
    print(" A: Yhteenlasku")
    print(" B: Vähennyslasku")
    print(" C: Kertolasku")
    print(" D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ").upper()

    if valinta == "Q":
        print("Kiitos laskimen käytöstä. Hei hei!")
        break

    if valinta in ("A", "B", "C", "D"):
        try:
            luku1 = float(input("Anna ensimmäinen luku: "))
            luku2 = float(input("Anna toinen luku: "))

            if valinta == "A":
                print(f"Tulos: {summa(luku1, luku2)}")
            elif valinta == "B":
                print(f"Tulos: {erotus(luku1, luku2)}")
            elif valinta == "C":
                print(f"Tulos: {tulo(luku1, luku2)}")
            elif valinta == "D":
                print(f"Tulos: {osamaara(luku1, luku2)}")

        except ValueError:
            print("Virhe: Syötä vain numeroita!")
    else:
        print("Virheellinen valinta, yritä uudelleen.")