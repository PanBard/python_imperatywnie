def main():
    name_file = "6_1.txt"
    out_file = open(name_file,'w')

    dane = input("Podaj imie i nazwisko: ")
    out_file.write(dane)
    print("Dane zapisano w pliku:",name_file)
    out_file.close()

    print()

    in_file = open(name_file,'r')
    dane_odczytane = in_file.read()
    print("Dane odczytano z pliku:",name_file)
    print("Zawartosc pliku: \n",dane_odczytane)
    in_file.close()

main()