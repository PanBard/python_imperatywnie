def znajdz_czworke_pitagorejska(przedzial):
    ilosc_iteracji = 0
    ilosc_czworek_zdublowanych = 0
    ilosc_samych_czworek = 0
    print("all:   once:")
    for a in range(1,przedzial):
        for b in range(1,przedzial):
            for c in range(1, przedzial):
                for d in range(1, przedzial):
                    ilosc_iteracji +=1

                    if a**2 + b**2 + c**2 == d**2 :
                        ilosc_czworek_zdublowanych +=1
                        print(a,",",b,",",c,",",d,"   ",end="",sep="")
                        if a**2 + b**2 + c**2 == d**2 and a < b :
                            ilosc_samych_czworek +=1
                            print(a,",", b,",", c,",",d, sep="")
                        else:
                            print()

    print(f"Ilosc iteracji: {ilosc_iteracji} \nIlosc trojek zdublowanych: {ilosc_czworek_zdublowanych} \nFaktyczna ilosc trojek: {ilosc_samych_czworek}")

def main():
    przedzial = int(input("Podaj gorny przedzial liczbowy: "))
    znajdz_czworke_pitagorejska(przedzial)
main()
