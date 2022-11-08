import math

def sum(N,period):
    all, k = 0,1
    while k <=N:
        all,k = all+period(k),k+1
    return all

def pi_term(i):
    return 8/((4*i-3)*(4*i-1))

def pi(N):
    return sum(N,pi_term)

def main():
    N = 1e6
    print("Calculate pi value: ",pi(N))
    print("Pi value from math module: ",math.pi)


if __name__ == '__main__':
    main()