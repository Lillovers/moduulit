kirjasto = {
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "Historiallinen romaani"],
    "Tuntematon sotilas": ["Väinö Linna", 1954, "Sotakirjallisuus"],
    "Seitsemän veljestä": ["Aleksis Kivi", 1870, "Klassikko"]
}
print(f"Sinuhen kirjoittaja: {kirjasto['Sinuhe egyptiläinen'][0]}")
print(f"Seitsemän veljeksen genre: {kirjasto['Seitsemän veljestä'][2]}")

kirjasto["Tuntematon sotilas"][2] = "Sotadraama"

kirjasto["Puhdistus"] = ["Sofi Oksanen", 2008, "Draama"]

del kirjasto["Seitsemän veljestä"]

print("\nKirjaston päivitetty sisältö:")
for kirja, tiedot in kirjasto.items():
    print(f"Kirja: {kirja} | Tiedot: {tiedot}")