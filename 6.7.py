def main():
    file_name = "6_5.txt"

    data_file = open(file_name, 'a')
    print("Program wyswietla rekordy odczytane z pliku",file_name)
    wybor = "y"

    while wybor == "y" or wybor =="Y":
        name = input("Imie: ")
        suranme = input("Podaj nazwisko; ")
        id_number = input("Podaj kod identyfikacyjny:")
        department = input("Podaj nazwe dzialu: ")

        data_file.write(name + "\n")
        data_file.write(suranme + "\n")
        data_file.write(id_number + "\n")
        data_file.write(department + "\n")

        wybor = input("Czy chcesz wprowadzic kolejny rekord?\nJesli tak wcisnij 'y', w przeciwnym przypadku inny klawisz: ")

    data_file.close()
main()