import  random

class Tablica_2_wymiarowa:
    def __init__(self):
        print("Obiekt klasy Tablica_2_wymiarowa zostal utworzony.")
        print()
        print("Umieszczenie na przekatnej tablicy 10x10 losowych liczb od 0 do 9")


    def __del__(self):
        print("\nObiekt klasy Tablica_2_wymiarowa zostal usuniety.")
        print("Zakonczenie programu")

    def zapelnij_tablice_i_narysuj(self,N,tablica):
        for i in range(N):
            for j in range(N):
                liczba = random.randint(1,9)
                if i==j:
                    tablica[i][j] = liczba
                else:
                    tablica[i][j] = 0

        for i in range(N):
            for j in range(N):
                print(tablica[i][j]," ",end="")
            print()

    def oblicz_sume_przekatnej(self,N,tablica):
        suma = 0
        for i in range(N):
            suma += tablica[i][i]
        print()
        print("Suma liczb na przekatnej = ",suma,".",sep="")

def main():
    N = 10
    tablica = [[0 for i in range(N)] for j in range(N)]
    macierz = Tablica_2_wymiarowa()
    macierz.zapelnij_tablice_i_narysuj(N,tablica)
    macierz.oblicz_sume_przekatnej(N,tablica)
    del macierz

main()








