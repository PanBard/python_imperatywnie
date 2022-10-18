def dodawanie(a,b):
    c = a + b
    return c

def odejmowanie(a,b):
    c = a - b
    return c

def mnozenie(a,b):
    c = a * b
    return c

def dzielenie(a,b):
    c = a / b
    return c



def main():
    a = float(input("Podaj pierwsza cyfre a= "))
    b = float(input("Podaj druga cyfre b= "))

    print(a,"+",b,"=",dodawanie(a,b))
    print(a,"-", b, "=",odejmowanie(a, b))
    print(a,"*", b, "=", mnozenie(a, b))
    print(a, "/", b, "=", dzielenie(a, b))
main()

