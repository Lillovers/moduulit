k = int(input("Anna kuhan pituus senttimetreinä? "))

if k <= 37:
    p = 37 - k
    print(f"Kuha on alimittainen. Laske se takaisin järveen")
    print(f"Pituudesta puuttuu {p} cm!")
else:
    print("Upea kala, tee siitä vaikka keitto. Voit pitää kuhan!")

