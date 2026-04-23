oppilaat = {
    "Elias": ["Elias", 7, "Matematiikka"],
    "Saga": ["Saga", 8, "Kuvataide"],
    "Otso": ["Otso", 9, "Historia"]
}
print(f"Eliaksen vuosiluokka: {oppilaat['Elias'][1]}")
print(f"Sagan lempiaine: {oppilaat['Saga'][2]}")

oppilaat["Otso"][2] = "Liikunta"

oppilaat["Lumi"] = ["Lumi", 7, "Biologia"]

del oppilaat["Saga"]

print("\nPäivitetty oppilaslista:")
for nimi, tiedot in oppilaat.items():
    print(f"{nimi}: {tiedot}")