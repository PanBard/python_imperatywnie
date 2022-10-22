def sumowanie_tego_ciagu(liczba_cyfr):
    suma = 0
    for x in range(liczba_cyfr):
        aktualna_liczba = x+1
        if aktualna_liczba == 1:
            suma = aktualna_liczba
        elif aktualna_liczba%2 == 0:
            suma += aktualna_liczba
        else:
            suma -= aktualna_liczba
    print(suma)

def main():
    liczba_cyfr = int(input("Podaj liczbe: "))
    sumowanie_tego_ciagu(liczba_cyfr)

main()

