l = float(input("Anna leviskät = "))
n = float(input("Annan naulat = "))
k = float(input("Anna luodit = "))
lg = 13.3
nl = 32
ln = 20
kl = (l*ln*nl+n*nl+k)
g = kl*lg
kg = int(g//1000)
jg = g%1000
print(f"Massa on {kg} kg ja {jg} g")