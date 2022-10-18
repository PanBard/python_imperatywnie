def pole(a,b):
    return a*b

def main():
    print("Elo w obliczatorze pola prostokata")

    a = float(input("Podaj bok a= "))
    b = float(input("Podaj bok b= "))


    print("Pole prostokata o boku a=",a,"i boku b=",b,"wynosi=",pole(a,b))



main()