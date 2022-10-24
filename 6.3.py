import random


file_name = "6_3.txt"
N = 10
tablica = [[0 for j in range(N)] for i in range(N)]
liczba_przekatna = 0
plik = open(file_name,'w')
for i in range(N): #liczba wierszow
    for j in range(N): #liczba kolumn
        ii = random.randint(1,10)
        jj = random.randint(1,10)
        if jj==j or ii==i:
            tablica[i][j] = 11
            liczba_przekatna +=1



        print(tablica[i][j], " ", end="")

    print()
plik.write(str(tablica))
plik.close()
print("liczby losowo ustawione: ",liczba_przekatna)
print()

plik2 = open(file_name,'r')
nowa_macierz = []
nowa_macierz= eval(plik2.readline())
print(nowa_macierz)
for i in range(N):
    for j in range(N):
        print(nowa_macierz[i][j]," ",end="")
    print()
plik2.close()


