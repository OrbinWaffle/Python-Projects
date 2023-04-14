# Name: Joshua Lai
# Project 3
# Completed 4/13/2022

usernames = []
passwords = []
specials = "[@_!#$%^&*()<>?/\|}{~:]"
def task_one_main():
    global usernames
    global passwords
    quitting = False
    while True:
        while True:
            new_name = input("\nPlease input a username (q to quit): ")
            if(new_name == "q"):
                quitting = True
                break
            if(verify_username(new_name) == True):
                break
        if(quitting):
            break
        while True:
            new_pass = input("\nPlease input a password (q to quit): ")
            if(new_pass == "q"):
                quitting = True
                break
            if(verify_password(new_pass) == True):
                break
        if(quitting):
            break
        usernames.append(new_name)
        passwords.append(new_pass)
        print("\nUser {0} created with password {1}".format(new_name, new_pass))
        ask_quit = input("\nDone? y/n: ")
        if(ask_quit == "y"):
            break
    user_dictionary = dict(zip(usernames, passwords))

    print("Welcome to the system.")
    while True:
        user_action = input("Input action (type \"help\" for a list of commands): ")
        if(user_action == "help"):
            print("login --- Log into the system."
                + "\nchangepass --- Change a password."
                + "\nnewuser --- Create a new user."
                + "\nquit --- Quit.")
    
# Takes in a string name and verifies that it is a valid username.
def verify_username(name):
    # Iterate through each character. If there is a letter, break to next section. Otherwise, return false.
    for char in name:
        if(char.isalpha()):
            break
    else:
        print("Invalid username. Must contain a letter.")
        return False
    # Iterate through usernames. If this username matches, return false. Otherwise, continue.
    for username in usernames:
        if(username == name):
            print("Invalid username. {0} already exists.".format(name))
            return False
    print("Username accepted.")
    return True

# Takes in a string password and verifies that it is a valid password.
def verify_password(password):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    has_eight = len(password) >= 8
    for char in password:
        if(not has_lower and char.islower()):
            has_lower = True
        if(not has_upper and char.isupper()):
            has_upper = True
        if(not has_digit and char.isdigit()):
            has_digit = True
        if(not has_special and char in specials):
            has_special = True
    if(has_lower and has_upper and has_digit and has_special and has_eight):
        print("Password accepted.")
        return True
    else:
        print("Invalid password.")
        if(not has_lower):
            print("Password must contain at least one lowercase letter.")
        if(not has_upper):
            print("Password must contain at least one uppercase letter.")
        if(not has_digit):
            print("Password must contain at least one digit.")
        if(not has_special):
            print("Password must contain at least one special character i.e. [@_!#$%^&*()<>?/\|}{~:]")
        if(not has_eight):
            print("Password must be at least eight characters long.")
        

def task_two_main():
    pass

def task_three_main():
    pass

# Task selector
while(True):
    selection = input("Which task would you like to run? Type 1, 2, or 3. Type q to quit: ")
    if (selection == "q"):
        quit()
    if (int(selection) == 1):
        task_one_main()
    elif (int(selection) == 2):
        task_two_main()
    elif (int(selection) == 3):
        task_three_main()
    print()