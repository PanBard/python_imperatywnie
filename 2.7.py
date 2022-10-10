

a = 5
b = 5
operacja = "dodawanie"



############# zwykly zapis##############


if operacja == "dodawanie":
    wynik = a + b

else:
    wynik = a - b

print("Wynik 1 metoda: ",wynik)

############### zapis operatorem trojargumentowym: ################

wynik = a + b if operacja == "dodawanie" else a - b

print("Wynik 2 metoda: ", wynik)
