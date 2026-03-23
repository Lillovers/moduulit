def poista_parittomat(lista):
    return [l for l in lista if l % 2 == 0]

def main():
    luvut = [1, 2, 3, 4, 5, 6, 7]
    karsittu = poista_parittomat(luvut)
    print("Alkuperäinen lista: ", luvut)
    print("Parilliset luvut: ", karsittu)

main()
    