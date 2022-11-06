from  datetime import datetime

def disable_function_in_night_time(function):
    def wrapper():
        if 6<= datetime.now().hour < 20:
            function()
            print("Ok this is right time, so you can see this. (between 6:00 and 20:00)" )
        else:
            print("dont work, because is night time ")
    return wrapper()

@disable_function_in_night_time
def display_message():
    print("Welcome!!")

def main():
    display_message

main()