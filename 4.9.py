def funkcja_rekurencyjna(i):
    if i > 0:
        print("Funkcja rekurencyjna zostala wywolana dla i=",i)
        funkcja_rekurencyjna(i-1)

def main():
    funkcja_rekurencyjna(5)

main()
