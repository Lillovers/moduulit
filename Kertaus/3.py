from math import sqrt

while True:
    luku = int(input("Anna numero: "))

    if luku < 0:
        print("Virheellinen numero")
    elif luku > 0:
        print(sqrt(luku))
    else:
        print("Exiting...")
        break