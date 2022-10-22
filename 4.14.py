def suma_zakresu_listy(lista, poczatek,koniec):
    if poczatek > koniec:
        return 0
    else:
        return lista[poczatek] + suma_zakresu_listy(lista,poczatek+1,koniec)

def main():
    lista_liczb=[1,2,3,4,5,6,7,8,9,10,11]
    print("Lista: ",lista_liczb)
    print()
    suma_liczb_z_listy_o_zadanym_zakresie = suma_zakresu_listy(lista_liczb,3,10)
    print("Suma elementow o indeksach od 3 do 10 wynosi: ",suma_liczb_z_listy_o_zadanym_zakresie)

main()