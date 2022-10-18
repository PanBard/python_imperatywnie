import random
import math
import datetime

def main():

    czas_startu = datetime.datetime.now()

    print("Aktualna data i czas systemu operacyjnego: ", czas_startu)

    punkty_generowane_w_kwadracie = int(input("Podaj ilość punktow generowanych w kwadracie: "))
    punkty_wygenerowane_tylko_w_kole = 0

    for i in range(1, punkty_generowane_w_kwadracie, 1):
        x = random.uniform(0,1)
        y = random.uniform(0,1)

        if x*x + y*y <= 1:
            punkty_wygenerowane_tylko_w_kole +=1

    print(punkty_wygenerowane_tylko_w_kole)

    obliczona_wartosc_pi = 4.0*punkty_wygenerowane_tylko_w_kole/punkty_generowane_w_kwadracie
    print(f"Wartość pi z modulu math.pi= {math.pi:.10f}")
    print(f"Wartość pi obliczona metoda monte carlo= {obliczona_wartosc_pi}")
    print(f"Błąd metody= {((abs(math.pi - obliczona_wartosc_pi)/math.pi)*100):.2f}%")

    czas_zakonczenia= datetime.datetime.now()

    czas_obliczen =  czas_zakonczenia - czas_startu
    print("Czas obliczeń wynosi= ",czas_obliczen, "s")

main()