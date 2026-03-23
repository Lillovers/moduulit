import random
def heita_noppaa():
    return random.randint(1, 6)

def main():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print("Heitit:", silmaluku)

main()