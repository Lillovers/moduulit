oikea_user = "python"
oikea_pass = "rules"

yritykset = 0

while yritykset < 5:
    user = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if user == oikea_user and salasana == oikea_pass:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")