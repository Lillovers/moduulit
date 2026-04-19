hinta = 5
kolikot = 0

while kolikot < 5:
    kolikot = kolikot + 1
    print("Annettu", kolikot, "kolikko")

while True:
    kolikot = kolikot + 1
    print("Annettu", kolikot, "euroa")
    if kolikot >= hinta:
        break

    print("Kahvi maksettu")