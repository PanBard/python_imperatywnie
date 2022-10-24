import random

class Macierz:
    file_name = "6_4.txt"

    def __init__(self):
        print("Obiekt klasy ¯\_(ツ)_/¯ zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy ¯\_(ツ)_/¯ zostal usuniety.")

    def save_data_in_file(self,dane_do_zapisania,name_file=file_name):
        dane_do_zapisania = str(dane_do_zapisania)
        with open(name_file,'w') as file:
            file.write(dane_do_zapisania)

    def read_data_from_file(self,name_file=file_name,dane_do_zapisania=0):
        new_matrix = []
        with open(name_file,'r') as file:
            new_matrix = eval(file.read())
        return new_matrix

    def generate_raw_matrix(self,size_of_matrix):
        matrix = [[0 for i in range(size_of_matrix)] for j in range(size_of_matrix)]
        return matrix

    def input_numbers_in_diagonal(self,matrix):
        size_of_matrix = len(matrix)
        for i in range(size_of_matrix):
            for j in range(size_of_matrix):
                if i == j:
                    matrix[i][j] = random.randint(1,9)

    def display_matrix_on_screen(self,matrix):
        size_of_matrix = 10
        for i in range(size_of_matrix):
            for j in range(size_of_matrix):
                print(matrix[i][j]," ",end="")
            print()

    def return_summation_numbers_in_diagonal(self,matrix):
        size_of_matrix = len(matrix)
        suma = 0
        for i in range(size_of_matrix):
            for j in range(size_of_matrix):
                if i==j:
                    suma += matrix[i][j]
        return suma

def main():
    m = Macierz()
    marix = m.generate_raw_matrix(10)
    m.input_numbers_in_diagonal(marix)
    m.save_data_in_file(marix)
    matrx_2 = m.read_data_from_file()
    m.display_matrix_on_screen(matrx_2)
    print("\nSuma liczb wystepujacych na przekatnej:",m.return_summation_numbers_in_diagonal(matrx_2))
main()



