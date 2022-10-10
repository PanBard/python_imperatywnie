
print("Prgoram sprawdza czy liczby a, b i c są trójką pitagorejską")
a = int(input("Podaj liczbę a:"))
b = int(input("Podaj liczbę b:"))
c = int(input("Podaj liczbę c:"))

print(a,b,c)

if a*a + b*b == c*c:
    print(f"Podane liczby: a={a}, b={b}, c={c} stanowia trojke pitagorejska")
else:
    print(f"Podane liczby: a={a}, b={b}, c={c} NIE stanowia trojki pitagorejskiej!!!")