sanat = ["kello", "auto", "lentokone", "koira", "saari", "haalari"]
laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"Listassa oli {laskuri} sanaa, joissa oli yli 5 kirjainta.")
