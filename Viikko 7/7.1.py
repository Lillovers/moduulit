def main():
    vuodenajat = ("talvi", "kevät", "kesä", "syksy")

    kuukausi = int(input("Anna kuukauden numero (1–12): "))

    if 1 <= kuukausi <= 12:
        vuodenaika_index = (kuukausi % 12) // 3
        print(vuodenajat[vuodenaika_index])
    else:
        print("Virheellinen kuukausi.")

if __name__ == "__main__":
    main()
