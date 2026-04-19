summa = 0

while True:
    luku = int(input("Anna, joku luku (-1 lopettaa): "))

    if luku == -1:
        break
    elif luku >= 10:
        continue

    summa += luku

print("Luku on", summa)