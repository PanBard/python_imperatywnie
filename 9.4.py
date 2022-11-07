
class MultiplicationByTwo:
    def __init__(self, number, limit_number):
        self.number = number
        self.limit_number = limit_number
        self.meter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.meter +=1
        value =  self.number * self.meter

        if value > self.limit_number:
            raise StopIteration
        else:
            return value

def main():
    number = float(input("Enter multiplication number: "))
    limit_result = int(input("Enter limit result number: "))


    for x in MultiplicationByTwo(number,limit_result):
        print(x)

if __name__ == '__main__':
    main()


