print("Program znajduje wrtosc x z rownania liniowego ax+b=c")

a = float(input("Podaj wartosc wspolczynnika a= \n"))

if a != 0:
    b = float(input("Podaj wartosc wspolczynnika b= \n"))
    c = float(input("Podaj wartosc wspolczynnika c=  \n"))

    x = (c -b)/a
    print(f"Wartosc szukanego x-sa wynosi: {x}")

else:
    print("Wspolczynnik a nie moze byc zerem!!!")
