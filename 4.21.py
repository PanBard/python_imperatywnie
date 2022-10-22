import math

def obliczanie_e(n):
    s,m = (1.0 , 1)
    for i in range(1, n):
        m = m*i
        s = s+(1.0/m)

    return s


def main():

    print(f"e z modulu math:           {math.e}")
    print(f"e obliczane przez program: {obliczanie_e(50)}")
main()

