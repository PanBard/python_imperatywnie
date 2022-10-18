from kalkulator import *

def main():
    print("Elo w kalkulatorze prostym")

    a = float(input("Podaj pierwsza liczbe a= "))
    b = float(input("Podaj druga liczbe b= "))

    rodziaj_dzialania = int(input("Podaj rodzaj dzialania: \n1 - dodawanie\n2 - odejmowanie\n3 - mnozenie\n4 - dzielenie\n"))

    if rodziaj_dzialania==1:
        print(a, "+", b, "=", dodawanie(a, b))
    elif rodziaj_dzialania == 2:
        print(a, "-", b, "=", odejmowanie(a, b))
    elif rodziaj_dzialania == 3:
        print(a, "*", b, "=", mnozenie(a, b))
    elif rodziaj_dzialania == 4:
        print(a, "/", b, "=", dzielenie(a, b))
    else:
        print("Nie ma tekiego numeru - uuu slabooo")



main()