class Osoba:

    def __init__(self):
        print("Obiekt klasy Osoba zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy Osoba zostal usuniety.")
        print("Zakonczenie programu")

    def czytaj_dane(self):
        self.imie = input("Podaj imie: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.ulica = input("Podaj adres: ")


    def wyswietl_dane(self):
        print("\nWyprowadzanie danych z programu \n")
        print("Imie:", self.imie)
        print("Nazwisko:",self.nazwisko)
        print("Adres:", self.ulica)

def main():
    Pracownik = Osoba()

    Pracownik.czytaj_dane()
    Pracownik.wyswietl_dane()

    del Pracownik

main()