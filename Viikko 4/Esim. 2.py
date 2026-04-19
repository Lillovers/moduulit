from sys import exc_info

kasky = input("Annetaanko lisää rahaa ('EI' lopettaa ohjelman)?").upper()

while kasky != "EI":
    print("Annetaan lisää rahaa")
    kasky = input("Annetaanko lisää rahaa?")

print("Ohjelma päättyy")