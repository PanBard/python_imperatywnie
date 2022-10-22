import random


class Sortowanie:
    def __init__(self):
        print("Obiekt klasy Sortowanie zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy Sortowanie zostal usuniety.")
        print("Zakonczenie programu")

    def pobierz_dane(self):
        a = int(input("Podaj ilosc liczb do wygenerowania: "))
        return a
    def generowanie_listy_losowych_liczb(self,liczba_cyfr):
        tablica = []
        for i in range(liczba_cyfr):
            tablica.append(random.randint(-999,999))
        return tablica

    def sortuj_liczby_w_liscie(self):
        pass

def main():
    sort = Sortowanie()
    print(sort.generowanie_listy_losowych_liczb(sort.pobierz_dane()))

main()

