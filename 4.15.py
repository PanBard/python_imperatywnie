def main():
    oblicz_funkcje = lambda x: x**2+1

    krok = 0.5
    x=0

    print("Program oblicza funkcje za pomoca funkcji lambda")
    print()

    while x<=5:
        y = oblicz_funkcje(x)
        print(f"dla x={x:.2f},   y = {y:.2f}")
        x +=krok

main()