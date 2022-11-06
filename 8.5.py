class SaveToFile:
    def __init__(self, name_file):
        self.name_file = name_file

    def __enter__(self):
        self.plik = open(self.name_file,'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.plik:
            self.plik.close()

    def writee(self, line):
        self.plik.write(line)

def main():
    with SaveToFile("8_5.txt") as new_file:
        new_file.writee("zapizsz to")
main()