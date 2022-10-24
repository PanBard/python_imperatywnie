class Student:
    file_name = "6_2.txt"
    def __init__(self):
        print("Obiekt klasy ¯\_(ツ)_/¯ zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy ¯\_(ツ)_/¯ zostal usuniety.")

    def zapisz_dane_do_pliku(self):
        outfile = open(self.file_name,'w')
        print(self.file_name)
        a = input("Podaj imie i nazwisko: \n")
        outfile.write(a)
        print("Dane zapisano w pliku",self.file_name)
        outfile.close()
        print()

    def odczytaj_dane_z_pliku(self):
        infile = open(self.file_name,'r')
        content_file = infile.read()
        print("Dane odczytane z pliku",self.file_name,":")
        print(content_file)
        infile.close()

def main():
    student1 = Student()
    student1.zapisz_dane_do_pliku()
    student1.odczytaj_dane_z_pliku()

main()