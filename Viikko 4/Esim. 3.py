kuha = int(input("Kuinka suuri kuha sait (negatiivinen lopettaa ohjelman)): "))

while kuha > 0:
    if kuha < 37:
        puutos = 37 - kuha
        print("Kuha on:", puutos, "senttiä liian lyhyt!")
    else:
        print("Hieno kuha")

    kuha = int(input("Kuinka suuri kuha on (negatiivinen lopettaa ohjelman): "))

print("Kuhalaskuri loppuu!")