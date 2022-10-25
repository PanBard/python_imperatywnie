def main():
    file_name = "6_5.txt"
    numbers_of_records = int(input("Podaj liczbe rekordow ktore maja zostac zapisane: "))
    print()
    data_file = open(file_name,'w')
    for i in range(1,numbers_of_records+1):
        print("Podaj dane o pracowniku nr",i)
        name = input("Imie: ")
        suranme = input("Podaj nazwisko; ")
        id_number = int(input("Podaj kod identyfikacyjny:"))
        department = input("Podaj nazwe dzialu: ")

