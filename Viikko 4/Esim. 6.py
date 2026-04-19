kasky = input("Annetaanko lisää rahaa (ei lopettaa): ")

while kasky != "ei":
    if kasky == "ryöstö":
        print("Rahat on ryöstetty")
        break
    print("Annettu 1 kolikko lisää")
    kasky = input("Annetaanko lisää rahaa (ei lopettaa): ")
else:
    print("Hyvästi")

print("Ohjelma loppuu...")
