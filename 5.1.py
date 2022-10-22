class Pole_prostokata:
    def __init__(self):
        print("Obiekt klasy Pole_prostokata zostal utworzony.")
        print()
        print("Program oblicza pole prostokata dla bokow a i b.")

    def __del__(self):
        print("Obiekt klasy Pole_prostokata zostal usuniety.")
        print("Zakonczenie programu")

    def wczytaj_dane(self):
        self.a = float(input("Podaj bok a: "))
        self.b = float(input("Podaj bok b: "))

    def oblicz_pole(self):
        self.pole = self.a * self.b
        return self.pole

    def wyswietl_co_tam_masz_do_wyswietlenia(self):
        print(f"Pole prostokata o boku a={self.a} i boku b={self.b} wynosi {self.pole}")
        print()

def main():
    pole = Pole_prostokata()

    pole.wczytaj_dane()
    pole.oblicz_pole()
    pole.wyswietl_co_tam_masz_do_wyswietlenia()

    del pole

main()
