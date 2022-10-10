import math

print("Oblicznaie pierwiastka kwadratowego")
print("dla dowolnych wspolczynnikow a, b, c")

a = float(input("Podaj wspolczynnik a= \n"))

if a != 0:
    b = float(input("Podaj wspolczynnik b= \n"))
    c = float(input("Podaj wspolczynnik c= \n"))

    print("Dla wprowadzonych liczb: ", end="")
    print("a = ",a," b = ",b," c = ", c)

    delta = b*b - 4*a*c

    if delta<0:
        print("dla delty rownej ",delta,"brak pierwiastkow rzeczywistych")
    elif delta == 0:
        x1 = -b/(2*a)
        print("Trojmian ma jeden pierwiastek podwojny: x1 =",x1)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("trojmian ma dwa pierwiastki: x1= ",x1," x2= ",x2)
else:
    print("Niedozwolona wartość wspolczynnika a !!!")




