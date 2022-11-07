def main():
    list_1 = list(range(10))
    list_2 = list(range(1, 10))
    list_3 = list(range(1, 10,1))

    print("Lista1=", list_1)
    for i in list_1:
        print(i)
    print()
    print("Lista2=", list_2)
    for i in list_2:
        print(i)
    print()
    print("Lista3=", list_3)
    for i in list_3:
        print(i)
    print()



if __name__ == '__main__':
    main()