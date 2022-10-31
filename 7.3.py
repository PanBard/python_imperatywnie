def main():
    file_name = "7_3.txt"

    personal_data = input("Enter name and surname: ")

    with open(file_name, 'w') as file:
        file.write(personal_data)
    print(f"Data is saved in the {file_name} file\n")

    entered_file_name = input("Enter file name for read: ")

    try:
        with open(entered_file_name,'r') as file1:
            contents_file = file1.read()
    except IOError:
        print("Invalid file name!")
    else:
        print(f"Data reads from {entered_file_name} file:\n{contents_file}")

main()