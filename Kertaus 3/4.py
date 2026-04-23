import math

def create_point(x, y):
    return (x, y)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

print("Anna ensimmäisen pisteen koordinaatit:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("\nAnna toisen pisteen koordinaatit:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

piste1 = create_point(x1, y1)
piste2 = create_point(x2, y2)

etaisyys = distance(piste1, piste2)

print(f"\nPisteiden {piste1} ja {piste2} välinen etäisyys on: {etaisyys:.2f}")