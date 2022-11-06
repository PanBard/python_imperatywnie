def big_letters(function):
    def wrapper():
        text = function()

        if not isinstance(text,str):
            raise TypeError("Podaj ciąg znaków.")
        return text.upper()
    return wrapper()

def main():

    @big_letters # dekorator
    def wydruk1():
        return "denmark okoncko"

    @big_letters
    def wydruk2():
        return "Enter words tu up letter: "

    print(f"Funkcja nr1: {wydruk1} ")
    print(f"Funkcja nr2: {wydruk2} ")
main()