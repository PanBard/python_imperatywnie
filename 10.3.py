def sum(N,period):
    all, k = 0,1
    while k <=N:
        all,k = all+period(k),k+1
    return all

def the_same(x):
    return x

def show_sum_natural_numbers(N):
    return sum(N,the_same)

def show_sum_natural_numbers_2(N):
    sum = 0
    for x in range(1,N+1):
        sum = x + sum
    return sum

def main():
    N=100
    print(show_sum_natural_numbers(N))
    print(show_sum_natural_numbers_2(N))
if __name__ == '__main__':
    main()