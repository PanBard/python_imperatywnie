def sprawdz_czy_tworza_trojke_pitagorejska(a,b,c):
    if a**2 + b**2 == c**2:
        print("TAK!!!!!")
        print("Zestaw liczb: a=",a,"b=",b,"c=",c,"na szczescie tworza trojke pitagorejska ")
    elif a**2 + c**2 == b**2:
        print("TAK!!!!!")
        print("Zestaw liczb: a=", a, "b=", b, "c=", c, "na szczescie tworza trojke pitagorejska")
    elif b**2 + c**2 == c**2:
        print("TAK!!!!!")
        print("Zestaw liczb: a=", a, "b=", b, "c=", c, "na szczescie tworza trojke pitagorejska")
    else:
        print("NIE!!!!")
        print("Zestaw liczb: a=",a,"b=",b,"c=",c,"nie tworza trojki pitagorejskiej :(")
def main():
    print("Program sprawdza czy podane liczby tworza trojke pitagorejska.")
    a = int(input("Podaj liczbe a= "))
    b = int(input("Podaj liczbe b= "))
    c = int(input("Podaj liczbe c= "))

    sprawdz_czy_tworza_trojke_pitagorejska(a,b,c)


main()