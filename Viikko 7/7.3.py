def main():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1) Syötä uusi lentoasema")
        print("2) Hae lentoaseman tiedot")
        print("3) Lopeta")

        valinta = input("Valinta: ")

        if valinta == "1":
            icao = input("Anna ICAO-koodi: ").upper()
            nimi = input("Anna lentoaseman nimi: ")
            lentoasemat[icao] = nimi
            print("Lentoasema tallennettu.")

        elif valinta == "2":
            icao = input("Anna ICAO-koodi: ").upper()
            if icao in lentoasemat:
                print(f"{icao}: {lentoasemat[icao]}")
            else:
                print("Lentoasemaa ei löydy.")

        elif valinta == "3":
            print("Ohjelma lopetettu.")
            break

        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()
