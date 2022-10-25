def main():
    file_name = "6_5.txt"

    data_file = open(file_name, 'r')
    print("Program wyswietla rekordy odczytane z pliku",file_name)

    name = data_file.readline()



    while name != "":
        surname = data_file.readline()
        nr_id = data_file.readline()
        dzial = data_file.readline()

        name = name.rstrip("\n")
        surname = surname.rstrip("\n")
        nr_id = nr_id.rstrip("\n")
        dzial = dzial.rstrip("\n")

        print("Imie i nazwisko: ", name)
        print("Nazwisko: ", surname)
        print("Nr identfikacyjny: ",nr_id)
        print("Dzial: ",dzial)
        print()

        name = data_file.readline()
    data_file.close()
main()