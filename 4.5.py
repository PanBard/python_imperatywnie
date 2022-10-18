import math


def oblicz_rownanie_kwadratowe(a, b, c):
    if a == 0:
        print("Jako wspolczynnik a podano 0, a mielismy bawic sie w funkcje kwadratowa :(")
        exit()
    else:
        delta = b ** 2 - 4 * a * c

        if delta < 0:
            print("Funkcja: ", a, "*X^2 + (", b, "*x) + (", c, ") posiada delte rowna: ", delta,
                  ", dlatego nie przecina sie z osia X (nie ma pierwaistkow)", sep="")
        if delta == 0:
            x1 = -b / (2 * a)
            print("Funkcja: ", a, "*X^2 + (", b, "*x) + (", c, ") posiada delte rowna: ", delta,
                  ", dlatego ma tylko jeden pierwiastek rowny = ", x1, sep="")
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print("Funkcja: ", a, "*X^2 + (", b, "*x) + (", c, ") posiada delte rowna: ", delta,
                  ", dlatego ma 2 pierwiastki: x1=", x1, " i x2=", x2, sep="")


def main():
    print("Podaj wspolczynniki funkcji kwadratowej:")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    oblicz_rownanie_kwadratowe(a, b, c)


main()
