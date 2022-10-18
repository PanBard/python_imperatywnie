def oblicz_sume_liczby_trojkatnej(x):
    if x == 1:
        return 1
    else:
        return x + oblicz_sume_liczby_trojkatnej(x-1)

def main():
    liczba_liczb_trojkatnych_do_obliczenia = int(input("Podaj ilosc liczb trojkatnych do oblczenia: "))

    for i in range(liczba_liczb_trojkatnych_do_obliczenia):
        print(f"liczba trojkatna nr{i+1} = {oblicz_sume_liczby_trojkatnej(i+1)}")

main()