def make_it_2_times(function):
    def run_it(value):
        return function(function(value))
    return run_it

def main():

    @make_it_2_times
    def some_function(x):
        return x+1

    print(some_function(1))

if __name__ == '__main__':
    main()