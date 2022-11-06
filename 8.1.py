def big_letters(function):
    text = function()

    if not isinstance(text,str):
        raise TypeError("Podaj ciąg znaków.")
    return text.upper()

def main():

    @big_letters # dekorator
    def wydruk():
        return int(input("Enter words tu up letter: "))
    print(wydruk)
main()