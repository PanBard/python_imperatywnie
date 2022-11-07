def simple_generator(number):

    while number >=0 :
        yield number
        number -=1


def main():
    print("Example of generator")

    for x in simple_generator(10):
        if x==0:
            print(x,end=" ")
        else:
            print(x,"->", end=" ")


if __name__ == '__main__':
    main()