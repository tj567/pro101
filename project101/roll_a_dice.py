import random

def roll():
    random_number = random.randint(1,6)
    if random_number == 1:
        print("[   ]")
        print("[ 0 ]")
        print("[   ]")
    elif random_number == 2:
        print("[0  ]")
        print("[   ]")
        print("[  0]")
    elif random_number == 3:
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
    elif random_number == 4:
        print("[0 0]")
        print("[   ]")
        print("[0 0]")
    elif random_number == 5:
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
    else:
        print("[0 0]")
        print("[0 0]")
        print("[0 0]")

def check_continue():
    user_response = input("enter 'y' to roll again, enter 'n' to stop ")
    if user_response == "y":
        return True
    elif user_response == "n":
        return False
    else:
        print("what are you doing bro?")

should_roll = True

while should_roll:
    roll()
    should_roll = check_continue()
