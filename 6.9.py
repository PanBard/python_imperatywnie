import os
class Modifier:
    file_name = "6_9.txt"
    temporary_file_name = "6_99.txt"
    change_status = False
    line_number = 0
    del_status = False

    def read_file_and_display_on_screen(self):
        state = input("Do you want to view the file? (yes-[press y],no-[press whatever])")
        if state == 'y' or state =='Y':
            data_file = open(self.file_name, 'r')
            print("Otwieranie pliku", self.file_name)

            name = data_file.readline()
            while name != "":
                surname = data_file.readline()
                nr_id = data_file.readline()
                dzial = data_file.readline()

                name = name.rstrip("\n")
                surname = surname.rstrip("\n")
                nr_id = nr_id.rstrip("\n")
                dzial = dzial.rstrip("\n")

                print("Imie i nazwisko: *",name,"*",sep="")
                print("Nazwisko: *", surname,"*",sep="")
                print("Nr identfikacyjny: *", nr_id,"*",sep="")
                print("Dzial: *", dzial,"*",sep="")
                print()

                name = data_file.readline()
            print("\nSign '*' is use to show invisible characters. ")
            data_file.close()
        else: print("Ok, so we continue")

    def record_scanning_or_modification(self):
        state = input("\nDo you want to search a word in the file, or modificate record? \nonly search - [press s] \nmodification - [press m] \ndelete - [press d] \nexit - [press whatever])")
        look_out_for = None
        change_phrase = None
        delete_phrase = None
        if state == "s" or state=="S":
            look_out_for = input("Enter the word you are looking for: ")
        elif state == "m" or state=="M":
            change_phrase = input("Enter the name and surname you want to modify: ")
            self.del_status = True
        elif state == "d" or state=="D":
            delete_phrase = input("Enter the name and surname you want to delete: ")
        else: exit(print("\nKoniec programu"))

        right_file = open(self.file_name,"r")
        temporary_file = open(self.temporary_file_name,'w')

        line = right_file.readline()
        while line != "":
            line = line.rstrip("\n")
            self.line_number += 1

            if change_phrase:
                if change_phrase == line:
                    new_word = input("Ok, we find this word.\n Enter new word: ")
                    temporary_file.write(new_word+"\n")
                    print("\nOld word [",line,"] has changed to new word [",new_word,"] in file:",self.file_name)
                    self.change_status = True
                else:
                    temporary_file.write(line+"\n")


            if look_out_for:
                if look_out_for == line:
                    print("Program found a words: [", look_out_for, "] in", self.line_number, "row in file:",self.file_name)

            if delete_phrase:
                if line != delete_phrase:
                    temporary_file.write(line+"\n")
                else:
                    self.del_status = True
            line = right_file.readline()

        right_file.close()
        temporary_file.close()

        if self.change_status:
            os.remove(self.file_name)
            print(f"File:{self.file_name} has removed. ")
            os.rename(self.temporary_file_name,self.file_name)
            print(f"File:{self.temporary_file_name} has changed name to {self.file_name}")
            print("File replacement procedure saccessfully completed.")
        elif self.del_status:
            os.remove(self.file_name)
            print(f"File:{self.file_name} has removed. ")
            os.rename(self.temporary_file_name, self.file_name)
            print(f"File:{self.temporary_file_name} has changed name to {self.file_name}")
            print(f"Delete record:[{delete_phrase}] procedure successfully completed.")
def main():
    agent = Modifier()
    agent.read_file_and_display_on_screen()
    agent.record_scanning_or_modification()

main()
