try:
    numero = int(input("Anna numero: "))
    jako = 10 /numero
    print("Arvo on", jako)
except ZeroDivisionError:
    print("Virhe, nollalla ei voi jakaa!")
except ValueError:
    print("Tuo ei ollut numero!")
finally:
    print("Tämä ajetaan aina")
print("Ohjelma suoritettu.")