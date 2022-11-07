
class MultiplicationByTwo:
    def __init__(self, number):
        self.number = number
        self.meter = 0

    def __next__(self):
        self.meter +=1
        return self.number * self.meter

def main():
    number = float(input("Enter multiplication number: "))
    how_many = int(input("Enter how many times: "))
    multiplication = MultiplicationByTwo(number)
    for x in range(how_many):
        print(next(multiplication))

if __name__ == '__main__':
    main()


