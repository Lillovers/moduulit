while True:
    tuumat = float(input("Anna tuumat (negatiivinen lopettaa): "))
    if tuumat < 0:
        print("Ohjelma päättyy.")
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {sentit:.2f} cm")