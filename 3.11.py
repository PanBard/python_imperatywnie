def main():

    ilosc_liczb_spelniajacych_warunek = 0

    for x in range(1000,10000, 1):
        pierwsze_dwie_cyfry = x // 100
        ostatnie_dwie_cyfry = x % 100

        if pierwsze_dwie_cyfry*pierwsze_dwie_cyfry + ostatnie_dwie_cyfry*ostatnie_dwie_cyfry == x:
            print(x,"=",pierwsze_dwie_cyfry,"*",pierwsze_dwie_cyfry,"+", ostatnie_dwie_cyfry,"*",ostatnie_dwie_cyfry )
            ilosc_liczb_spelniajacych_warunek +=1

    print("Znaleziono", ilosc_liczb_spelniajacych_warunek, "takie liczby.")








main()