def fibonaci_generator():
    new_fib_number , old_fib_number = 1 ,0
    yield old_fib_number
    yield new_fib_number

    while True:
        new_fib_number, old_fib_number = old_fib_number + new_fib_number,new_fib_number
        yield new_fib_number

def main():
    amonunt = 10
    fib = fibonaci_generator()

    for i in fib:
        print(i)

        if i > amonunt:
            break

    print("Next generated number with __next__ function: ",fib.__next__())



if __name__ == '__main__':
    main()