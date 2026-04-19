luokka = input("Mikä hyttiluokka LUX, A, B vai C? ").upper()

if luokka == "A" :
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif luokka == "LUX" or "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka.")