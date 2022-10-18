def ciag_fibonacciego(ilosc):
    if ilosc==0:
        return 0
    elif ilosc == 1:
        return 1
    else:
        return ciag_fibonacciego(ilosc-1) + ciag_fibonacciego(ilosc-2)

def main():

    ilosc_liczb_ciagu = int(input("Podaj ilosc liczb ciagu fibonaczJego: "))

    for i in range(ilosc_liczb_ciagu):
        print(",",ciag_fibonacciego(i+1),end="")

main()