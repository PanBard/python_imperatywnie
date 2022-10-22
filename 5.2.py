import math

class Obliczacz_pierwiastka_kwadratowego():
    def __init__(self):
        print("Obiekt klasy Obliczacz_pierwiastka_kwadratowego zostal utworzony.")
        print()
        print("Oblicznaie pierwiastka kwadratowego")
        print("dla dowolnych wspolczynnikow a, b, c")

    def __del__(self):
        print("\n Obiekt klasy Obliczacz_pierwiastka_kwadratowego zostal usuniety.")
        print("Zakonczenie programu")

    def wczytaj_dane(self):
        self.a = float(input("Podaj wspolczynnik a= "))
        if self.a != 0:
            self.b = float(input("Podaj wspolczynnik b= "))
            self.c = float(input("Podaj wspolczynnik c= "))
        else:
            print("Niedozwolona wartość wspolczynnika a !!!")

    def oblicz_delte_funkcji(self):
        self.delta = self.b * self.b - 4 * self.a * self.c

    def oblicz_pierwiastki_i_wypisz_wyniki(self):

        if self.delta < 0:
            print("dla delty rownej ", self.delta, "brak pierwiastkow rzeczywistych")
        elif self.delta == 0:
            x1 = -self.b / (2 * self.a)
            print("dla delty rownej ", self.delta,", trojmian ma jeden pierwiastek podwojny: x1 =", x1)
        else:
            x1 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            print("dla delty rownej ", self.delta," trojmian ma dwa pierwiastki: x1= ", x1, " x2= ", x2)


def main():
    kalkulatorek_funkcji_kwadratowej = Obliczacz_pierwiastka_kwadratowego()

    kalkulatorek_funkcji_kwadratowej.wczytaj_dane()
    kalkulatorek_funkcji_kwadratowej.oblicz_delte_funkcji()
    kalkulatorek_funkcji_kwadratowej.oblicz_pierwiastki_i_wypisz_wyniki()

    del kalkulatorek_funkcji_kwadratowej


main()






