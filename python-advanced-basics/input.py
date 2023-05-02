import datetime

def get_user_input():
    name = input("Hey there! What's your name: ")
    age = int(input("Great now what's your age: "))
    return name, age

def time_to_100(age):
    return 100 - age

def future_date(current_date, time):
    return current_date + time_to_100()

current_date = datetime.datetime.now().year
name, age = get_user_input()

while age > 100:
    print("C'mon! you can't be that old")
    name, age = get_user_input()
    
print("Whoaa {}, did you know you will turn 100 years-old in {:d}, \n Thats {} in years!".format(name, year, time))