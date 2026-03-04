nimi = input("Anna nimesi: ")

if nimi != "Matti":
    annokset = int(input("Kuinka monta keittoannosta haluat? "))
    hinta = annokset * 5.90
    print(f"Kokonaishinta on {hinta} euroa.")
else:
    print("Seuraava, kiitos!")