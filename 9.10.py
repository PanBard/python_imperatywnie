def generate_prime_numbers(N):
    prime_numers_list = []

    for i in range(2,N):
        for j in prime_numers_list:
            if i%j == 0:
                break
        else:
            yield i
            prime_numers_list.append(i)

def main():
    N = 150

    print("Program generate prime number in range from 2 to",N,"\n")

    gen = generate_prime_numbers(N)

    for i in gen:
        print(i,end=", ")

if __name__ == '__main__':
    main()
