import pickle

class Osoba:
    file_name = "6_12.b"

    def __init__(self):
        print("Obiekt klasy Osoba zostal utworzony.")
        print()


    def __del__(self):
        print("\nObiekt klasy Osoba zostal usuniety.")


    def czytaj_dane(self):
        self.imie = input("Podaj imie: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.ulica = input("Podaj adres: ")
        self.dane = self.nazwisko + self.imie + self.ulica
        print("Mada: ",self.dane)

    def save_data_in_binary_file(self):
        with open(self.file_name,'wb') as file:
            pickle.dump(self.dane,file)

    def load_data_from_binary_file(self):
        with open(self.file_name,'rb') as file2:
            self.data_file = pickle.load(file2)
            print(self.data_file)

    def wyswietl_dane(data_file):
        print("\nWyprowadzanie danych z programu \n")
        print("Imie:", data_file.imie)
        print("Nazwisko:", data_file.nazwisko)
        print("Adres:", data_file.ulica)


def main():
    Pracownik = Osoba()
    Pracownik.czytaj_dane()
    Pracownik.save_data_in_binary_file()
    Pracownik.load_data_from_binary_file()
    Pracownik.wyswietl_dane()

    del Pracownik

main()