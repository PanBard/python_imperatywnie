import math

def dodaj_do(x):
    def dodaj(y):
        return x+y
    return dodaj



def main():
    dodaj_do_15 = dodaj_do(15)

    print("Wynik: ",dodaj_do_15(20))
main()

