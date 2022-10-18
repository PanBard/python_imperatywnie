def najwiekszy_wspolny_dzielnik(a,b):
    if a%b ==0:
        return b
    else:
        return najwiekszy_wspolny_dzielnik(b, a%b)

def main():
    a = int(input("Podaj pierwsza liczbe calkowita:"))
    b = int(input("Podaj druga liczbe calkowita:"))

    print(f"Najwiekszy wspolny dzielnik dla liczb: {a} i {b} wynosi: {najwiekszy_wspolny_dzielnik(a,b)}")

main()