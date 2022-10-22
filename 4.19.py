def sumowanie_tego_ciagu(liczba_cyfr):
    suma = 0
    for x in range(1, liczba_cyfr+1):
        suma += 2*x-1
    print(suma)

def main():
    liczba_cyfr = int(input("Podaj liczbe: "))
    sumowanie_tego_ciagu(liczba_cyfr)
main()

