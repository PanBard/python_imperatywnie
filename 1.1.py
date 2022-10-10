
print("Program oblicza pole prostokąta.")

a = float(input("Podaj bok a: "))     #czytanie z klawiatury liczby rzeczywistej
b = float(input("Podaj bok a: "))     #czytanie z klawiatury liczby rzeczywistej

print() # wyswietla pusta linie

pole = a * b

print("Dla a =",a,"i b =",b)
print("Pole prostokata: ",pole)

#lub sformatowany łańcuch znaków - f-łańcuch

print(f"Dla a ={a} i b ={b}")
print(f"Pole prostokąta: {pole}")

