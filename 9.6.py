def my_generator(number,limit):
    counter = 1
    value = number*counter

    while value <= limit:
        yield value
        counter +=1
        value = number*counter

def main():
    print("Example of generator")

    for x in my_generator(500,4000):
        print(x)

if __name__ == '__main__':
    main()