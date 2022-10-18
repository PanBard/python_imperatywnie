def wylicz_wartosc_fnkcji(x):
    return x**2 +1

def main():

    x=0
    krok = 0.5
    while x <=5:
        y = wylicz_wartosc_fnkcji(x)
        print(f"dla x={x:.3f}, y={y:.3f}")
        x += krok

main()