# Name: Joshua Lai
# Project 3
# Completed 4/13/2022

usernames = []
passwords = []
specials = "[@_!#$%^&*()<>?/\|}{~:]"
def task_one_main():
    global usernames
    global passwords
    user_file = open("users.txt", "r")
    pass_file = open("passwords.txt", "r")
    for new_name in user_file:
        new_name = new_name.rstrip("\n")
        if(verify_username(new_name, False) == True):
            usernames.append(new_name)
        else:
            continue
        new_pass = pass_file.readline()
        new_pass = new_pass.rstrip("\n")
        if(verify_password(new_pass, False) == True):
            passwords.append(new_pass)
        else:
            continue
        # print("\nUser {0} created with password {1}".format(new_name, new_pass))
    user_dictionary = dict(zip(usernames, passwords))

    print("Welcome to the system. Type \"help\" for a list of commands.")
    while True:
        user_action = input("> ")
        match user_action:
            case "help":     
                print("\nlogin --- Log into the system."
                    + "\nchangepass --- Change a password."
                    + "\nnewuser --- Create a new user."
                    + "\nq --- Quit.")
            case "q":
                break
            case "login":
                login_result = login(user_dictionary)
                if(login_result[0]):
                    print("Successfuly logged in. Welcome, {0}.".format(login_result[1]))
                else:
                    print("Unable to log in.")
            case "changepass":
                if(change_pass(user_dictionary)):
                    print("Password successfuly changed.")
                else:
                    print("Password change was unsuccessful.")
            case "newuser":
                new_username = create_user(user_dictionary)
                if(not new_username is None):
                    print("Welcome, {0}.".format(new_username))
            case _:
                print("Unrecognized command. Type \"help\" for a list of commands.")
    
# Takes in a string name and verifies that it is a valid username.
def verify_username(name, print_text = True):
    # Iterate through each character. If there is a letter, break to next section. Otherwise, return false.
    for char in name:
        if(char.isalpha()):
            break
    else:
        if(print_text): print("{0} is an invalid username. Must contain a letter.".format(name))
        return False
    # Iterate through usernames. If this username matches, return false. Otherwise, continue.
    for username in usernames:
        if(username == name):
            if(print_text): print("Invalid username. \"{0}\" already exists.".format(name))
            return False
    if(print_text): print("Username accepted.")
    return True

# Takes in a string password and verifies that it is a valid password.
def verify_password(password, print_text = True):
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
        if(print_text): print("Password meets requirements.")
        return True
    else:
        if(not print_text): return False
        print("\"{0}\" is an invalid password.".format(password))
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
        return False

def login(user_dict):
    for user_tries in range(3):
        username = input("\nPlease input your username: ")
        try:
            password = user_dict[username]
            for pass_tries in reversed(range(3)):
                input_password = input("\nPlease input your password: ")
                if(input_password == password):
                    return (True, username)
                else:
                    print("Incorrect password. {0} {1} remaining.".format(pass_tries, "try" if pass_tries == 1 else "tries"))
            else:
                print("Login unsucessful after 3 tries.")
                return (False, "")
        except LookupError:
            print("Unable to find user \"{0}.\" Please try again.".format(username))
    else:
        print("Unable to find user after three tries.")
        return (False, "")

def create_user(user_dict):
    while (True):
        new_username = input("\nPlease input your new username: ")
        if(verify_username(new_username) == True):
            pass
        else:
            continue
        while (True):
            new_pass = input("\nPlease input your new password: ")
            if(verify_password(new_pass)):
                check_pass = input("\nVerify your password: ")
                if(new_pass == check_pass):
                    user_dict[new_username] = new_pass
                    return (new_username)
                else:
                    print("Passwords do not match. Please try again.")


def change_pass(user_dict):
    login_result = login(user_dict)
    if(login_result[0]):
        while (True):
            new_pass = input("\nPlease input your new password: ")
            if(verify_password(new_pass)):
                check_pass = input("\nVerify your password: ")
                if(new_pass == check_pass):
                    user_dict[login_result[1]] = new_pass
                    return True
                else:
                    print("Passwords do not match. Please try again.")
    else:
        return False

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