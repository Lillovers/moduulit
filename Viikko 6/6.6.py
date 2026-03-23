import math

def pizzan_yksikkohinta(halkaisija_cm, hinta):
    sade = halkaisija_cm / 2
    pinta_ala_m2 = math.pi * (sade ** 2) / 10000
    return hinta / pinta_ala_m2

def main():
    print("Anna ensimmäisen pizzan tiedot:")
    d1 = float(input("Halkaisija (cm): "))
    h1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    d2 = float(input("Halkaisija (cm): "))
    h2 = float(input("Hinta (€): "))

    y1 = pizzan_yksikkohinta(d1, h1)
    y2 = pizzan_yksikkohinta(d2, h2)

    print(f"\nPizza 1: {y1:.2f} €/m²")
    print(f"Pizza 2: {y2:.2f} €/m²")

    if y1 < y2:
        print("Pizza 1 antaa paremman vastineen rahalle.")
    else:
        print("Pizza 2 antaa paremman vastineen rahalle.")

main()
