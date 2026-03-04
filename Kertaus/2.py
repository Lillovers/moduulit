tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ")

if paiva == "sunnuntai":
    paivapalkka = 2 * tuntipalkka * tunnit
else:
    paivapalkka = tuntipalkka * tunnit

print(f"Päiväpalkka: {paivapalkka} euroa")