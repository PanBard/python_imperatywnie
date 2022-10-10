
wielkosc_tabliczki = int(input("Podaj jak wielka powinna byc tabliczka: "))

for kolumny in range(wielkosc_tabliczki):
    for wiersze in range(wielkosc_tabliczki):
        print((wiersze +1)*(kolumny+1),"\t",end="")
    print()

