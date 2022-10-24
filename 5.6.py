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

class Pracownik(Osoba):
    def __init__(self):
        print("Obiekt klasy Pracownik zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy Pracownik zostal usuniety.")
        print("Zakonczenie programu")

    def pomachaj_ogonem(self):
        print("Mahatam ogoniastym")

def main():
    czlowiek = Osoba()
    robotnik = Pracownik()

    print("Dla czlowieka:")
    czlowiek.czytaj_dane()
    czlowiek.wyswietl_dane()

    print("Dla robotnika:")
    robotnik.czytaj_dane()
    robotnik.wyswietl_dane()
    robotnik.pomachaj_ogonem()

    del robotnik
    del czlowiek
main()
