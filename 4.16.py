def znajdz_trojke_pitagorejska(przedzial):
    ilosc_iteracji = 0
    ilosc_trojek_zdublowanych = 0
    ilosc_samych_trojek = 0
    print("all:   once:")
    for a in range(1,przedzial):
        for b in range(1,przedzial):
            for c in range(1, przedzial):
                ilosc_iteracji +=1

                if a**2 + b**2 == c**2:
                    ilosc_trojek_zdublowanych +=1
                    print(a,",",b,",",c,"   ",end="",sep="")
                    if a**2 + b**2 == c**2 and a > b:
                        ilosc_samych_trojek +=1
                        print(a,",", b,",", c, sep="")
                    else:
                        print()

    print(f"Ilosc iteracji: {ilosc_iteracji} \nIlosc trojek zdublowanych: {ilosc_trojek_zdublowanych} \nFaktyczna ilosc trojek: {ilosc_samych_trojek}")





def main():
    przedzial = int(input("Podaj gorny przedzial liczbowy: "))
    znajdz_trojke_pitagorejska(przedzial)
main()
