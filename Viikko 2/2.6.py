import random
k1 = ""
for _ in range(3):
    k1 += str(random.randint(0, 9))
k2 = ""
for _ in range(4):
    k2 += str(random.randint(1, 6))

print("Kolminumeroinen koodi:", k1)
print("Nelinumeroinen koodi:", k2)
