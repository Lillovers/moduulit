numero = int(input("Anna numero välillä 1-10: "))

print(f"Luvun {numero} kertotaulu: ")
for i in range(1, 11):
    tulo = numero * i
    print(f"{numero} x {i} = {tulo}")