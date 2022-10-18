import math

def main():
    dolna_granica_przedialu = int(input("Podaj dolna granice przedzialu: "))
    gorna_granica_przedialu = int(input("Podaj gorna granice przedzialu: "))

    print("Liczby pierwsze z przedzialu od",dolna_granica_przedialu,"do", gorna_granica_przedialu,"to: ")
    gorna_granica_przedialu += 1
    for x in range(dolna_granica_przedialu,gorna_granica_przedialu):
        if all(x%i != 0 for i in range(2, int(math.sqrt(x))+1)):
            print(x,",",sep="",end="")



main()