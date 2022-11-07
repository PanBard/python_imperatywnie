def odd_number_generator(scope):
    odd_number = 1
    while odd_number <= scope:
        if odd_number%2 != 0:
            yield odd_number
        odd_number+=1


def main():
    print("Example of generator")

    gen = odd_number_generator(100)
    print(list(gen))


if __name__ == '__main__':
    main()