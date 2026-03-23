import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def main():
    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))
    silmaluku = 0
    while silmaluku != tahkojen_maara:
        silmaluku = heita_noppaa(tahkojen_maara)
        print(silmaluku)

main()
        