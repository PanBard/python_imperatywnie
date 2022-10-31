import  pickle

def main():
    file_name = "6_13.txt"

    print("Program zapisuje dane ksiazek z domowej biblioteki")

    one_book_data = []
    all_book_data = {}

    one_book_data.append(input("Enter author name: "))
    one_book_data.append(input("Enter auhtor surname: "))
    one_book_data.append(input("Enter book title: "))

    all_book_data = {1: one_book_data}

    print("\nEntered books data:",all_book_data)

    with open(file_name,'wb') as file1:
        pickle.dump(all_book_data,file1)

    with open(file_name,'rb') as file2:
        dictionary_copy = pickle.load(file2)

    print("\nBooks data from file:",dictionary_copy)

main()