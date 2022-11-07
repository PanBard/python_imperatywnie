def main():
    list = [1,2,3,4,5,6]
    tuple = (1,2,3,4,5,6)
    string = "Krzysztof"

    for x in list:
        print(x**2," ",end="")
    print()

    for x in tuple:
        print(x**2," ",end="")
    print()

    for x in string:
        print(x*5," ",end="")

main()