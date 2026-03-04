tarina = []

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana == "loppu":
        break

    tarina.append(sana)

print(" ".join(tarina))