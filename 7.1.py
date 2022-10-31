def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multipication(a,b):
    return a*b
def division(a,b):
    return a/b

def main():
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))

    print(a, "+",b,"=",add(a,b),".")
    print(a, "-", b, "=", subtract(a, b), ".")
    print(a, "*", b, "=", multipication(a, b), ".")

    try:
        print(a, ":", b, "=", division(a, b), ".")

    except ZeroDivisionError:
        print("Division by 0!!!!")

main()