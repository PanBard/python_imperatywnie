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

    def sortuj_liczby_w_liscie(self,liczby):
        for i in range(len(liczby)-1,0,-1):
            for j in range(i):
                if liczby[j] >liczby[j+1]:
                    liczby[j],liczby[j+1] = liczby[j+1],liczby[j]
        return liczby
    def wyswietl_wyniki(self, lista_przed,lista_po):
        print("Liczby nieposortowane:",lista_przed)
        print("Liczby posortowane: ",lista_po)


def main():
    sort = Sortowanie()

    lista_nieposortowana = sort.generowanie_listy_losowych_liczb(sort.pobierz_dane())
    lista_nieposortowana_2 = lista_nieposortowana.copy()
    lista_posortowana = sort.sortuj_liczby_w_liscie(lista_nieposortowana)
    sort.wyswietl_wyniki(lista_nieposortowana_2,lista_posortowana)

main()

