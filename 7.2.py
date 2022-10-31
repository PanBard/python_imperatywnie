import math

class Calculation:

    def root_of_quadratic_function(self,a,b,c):

        print(f"For entered numbers:\na={a} , b ={b} , c={c}\n")

        delta = b**2 - 4*a*c

        if delta < 0:
            print(f"Delta = {delta}, so this function have not the root")
        elif delta == 0:
            x1 = -b/(2*a)
            print(f"Delta = {delta}, so function have one root: x1 ={x1} ")
        else:
            x1 = (-b - math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            print(f"Delta = {delta}, so this function has two root: x1={x1}, x2={x2}")

def main():
    calc = Calculation()
    a = float(input("This program calculate the root of the square function\nEnter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    try:
        calc.root_of_quadratic_function(a,b,c)
    except ZeroDivisionError:
        print("Prohibited value of 'a' factor - 'a' can't be 0")
main()
