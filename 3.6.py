# liczba_ileracji_wartosci_funkcji = int(input("Podaj liczbe powtorzen:  "))
#
# for x in range(liczba_ileracji_wartosci_funkcji):
#     wynik = liczba_ileracji_wartosci_funkcji * 3
#     print("x=", liczba_ileracji_wartosci_funkcji, " y=", wynik)
#     liczba_ileracji_wartosci_funkcji -= 1

############### lub:

print("Program oblicza wartosci funkcji y=3*x")
print("dla x zmieniajacych sie od 1 do 10")

lista = list(range(1,11,1))

print("Lista= ",lista)

for x in lista:
    y = 3*x
    print("dla x=",x,"y=",y)



