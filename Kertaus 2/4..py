def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(koko):
        valilyonnit = " " * (koko - i - 1)
        tahdet = "*" * (2 * i + 1)
        print(valilyonnit + tahdet)

    print(" " * (koko - 1) + "*")

kuusi(5)