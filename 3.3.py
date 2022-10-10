
liczba = 2

suma = 0
while liczba <= 100:
    print(liczba,", ", end="")

    if liczba%2 == 0:
        suma += liczba
    liczba += 1

print("\nSuma liczb parzystych od 1 do 100 wynosi=",suma)