def make_it_2_times(function):
    def run_it(value):
        return function(function(value))
    return run_it

def main():
    add = lambda data: data + 1
    result=make_it_2_times(add)
    print(result(1))

if __name__ == '__main__':
    main()