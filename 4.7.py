import random

def generowanie_listy_10_liczb_losowych():
    liczby =[]
    for x in range(10):
        liczba_losowa = random.randint(-100,100)
        liczby.append(liczba_losowa)
    return liczby


def sortowanie_listy_liczb(liczby):
    print("Przed:",liczby)
    for i in range(len(liczby)-1,0,-1):

        for j in range(i):

            if liczby[j] > liczby[j+1]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j]

    print("Po:",liczby)

def main():
    sortowanie_listy_liczb(generowanie_listy_10_liczb_losowych())

main()

