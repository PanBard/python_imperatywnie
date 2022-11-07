import itertools

def main():
    print("Program shows how works iterator:\n")

    list = ["Ząb","za","ząb"]

    iterator = itertools.cycle(list)

    for i in range(9):
        print(next(iterator),end=" ")

main()