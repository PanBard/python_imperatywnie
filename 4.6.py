def funkcja_signum(liczba):
    if liczba > 0:
        wartosc_signum = 1
    elif liczba == 0:
        wartosc_signum = 0
    else:
        wartosc_signum = -1
    print("Dla podanej liczby:",liczba,"wartosc funkcji signum wynosi:",wartosc_signum)

def main():
    liczba = int(input("Podaj liczbe, a zostanie zwrocona wartosc z funkcji signum: "))
    funkcja_signum(liczba)

main()