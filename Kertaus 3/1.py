kayttajat = {
    "John": ["John", 30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna": ["Anna", 22, "Student"]
}
print(f"Johnin nimi: {kayttajat['John'][0]}, ikä: {kayttajat['John'][1]}")
print(f"Emilyn ammatti: {kayttajat['Emily'][2]}")

kayttajat["Anna"][2] = "Teacher"
kayttajat["James"] = ["James", 28, "Writer"]

kayttajat["Sophia"] = ["Sophia", 35, "Doctor"]

del kayttajat["Emily"]

print("\nLopullinen sanakirja:")
for avain, tiedot in kayttajat.items():
    print(f"{avain}: {tiedot}")