def gallonat_litroiksi(gallont):
    return gallont * 3.785

def main():
    while True:
        g = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
        if g <= 0:
            break
        litrat = gallonat_litroiksi(g)
        print(f"{g} gallonaa = {litrat:.3f} litraa")

main()