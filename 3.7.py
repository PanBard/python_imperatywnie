import random
liczba_losowanych_liczb = int(input("Podaj ilosc liczb do wylosowania: "))
print("Wygenerowane losowo liczby to: ", end="")
min = 100
max = 0
suma_liczb=0

for x in range(liczba_losowanych_liczb  ):

    wylosowana_liczba = random.randint(1,100)
    print(wylosowana_liczba, ", ", end="")

    if wylosowana_liczba > max:
        max = wylosowana_liczba
    if wylosowana_liczba < min:
        min = wylosowana_liczba
    suma_liczb += wylosowana_liczba
srednia_wszystkich_liczb = suma_liczb/liczba_losowanych_liczb
srednia_min_max = (min+max)/2
print()
print("najwieksza liczba = ", max)
print("najmniejsza liczba = ", min)
print("srednia ze wszystkich liczb=", srednia_wszystkich_liczb)
print("srednia z 2 ekstremow (min i max)=", srednia_min_max)
