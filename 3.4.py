
liczba = 1

suma = 0
while liczba <= 100:


    if not (liczba%2 == 0):
        suma += liczba
        print(liczba, ", ", end="")
    liczba += 1


print("\nSuma liczb nieparzystych od 1 do 100 wynosi=",suma)