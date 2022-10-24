import math
class Pole_figury:

    def __init__(self):
        print("Obiekt klasy \_~..~_/ zostal utworzony.")
        print()
        print("")

    def __del__(self):
        print("\nObiekt klasy \_~..~_/ zostal usuniety.")

    def oblicz_pole(self):
        print()

class Pole_prostokata(Pole_figury):
    def oblicz_pole(self):
        self.a = int(input("Podaj dlugosc boku a: "))
        self.b = int(input("Podaj dlugosc boku b: "))
        pole = self.a * self.b
        print("Pole prostokata:",pole)

class Pole_trojkata(Pole_figury):
    def oblicz_pole(self):
        self.a = int(input("Podaj dlugosc podstawy a: "))
        self.h = int(input("Podaj wysokosc h: "))
        pole = self.a * 0.5 * self.h
        print("Pole trojkata:",pole)

class Pole_kola(Pole_figury):
    def oblicz_pole(self):
        self.a = int(input("Podaj dlugosc promienia r: "))
        pole = self.a**2 * math.pi
        print("Pole kola:",pole)

class Pole_trapezu(Pole_figury):
    def oblicz_pole(self):
        self.a = int(input("Podaj dlugosc podstawy a: "))
        self.b = int(input("Podaj dlugosc podstawy b: "))
        self.h = int(input("Podaj wysokosc h: "))
        pole = (self.a+self.b)*self.h*0.5
        print("Pole trapezu:",pole)

def main():
    wybor = int(input("Co chcesz obliczyc:\n1-pole prostokata\n2-pole trojkata\n3-pole kola\n4-pole trapezu\n(wybierz numerek):"))
    if wybor==1:
        pole = Pole_prostokata()
        pole.oblicz_pole()
    elif wybor==2:
        pole = Pole_trojkata()
        pole.oblicz_pole()
    elif wybor==3:
        pole = Pole_kola()
        pole.oblicz_pole()
    elif wybor==4:
        pole = Pole_trapezu()
        pole.oblicz_pole()

main()