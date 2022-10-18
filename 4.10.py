def oblicz_silnie(x):
    if x == 0:
        return 1
    else:
        return x * oblicz_silnie(x-1)


def main():
    liczba = int(input("Podaj z jakiej liczby chcesz obliczyc silnie: "))
    print(f"Silnia z {liczba} jest rowna {oblicz_silnie(liczba)}")

    for i in range(liczba+1):
        print(f"!{i} = {oblicz_silnie(i)}")


main()