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
            pass
        else:
            continue
        new_pass = pass_file.readline()
        new_pass = new_pass.rstrip("\n")
        if(verify_password(new_pass, False) == True):
            usernames.append(new_name)
            passwords.append(new_pass)
        else:
            continue
    user_file.close()
    pass_file.close()
    user_dictionary = dict(zip(usernames, passwords))

    print("\nWelcome to the system. Type \"help\" for a list of commands.")
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

    # TASK ONE OUTPUT:

    # Which task would you like to run? Type 1 or 2. Type q to quit: 1

    # Welcome to the system. Type "help" for a list of commands.
    # > help

    # login --- Log into the system.
    # changepass --- Change a password.
    # newuser --- Create a new user.
    # q --- Quit.
    # > login

    # Please input your username: gogo
    # Unable to find user "gogo." Please try again.

    # Please input your username: danny

    # Please input your password: hi
    # Incorrect password. 2 tries remaining.

    # Please input your password: ho
    # Incorrect password. 1 try remaining.

    # Please input your password: ha
    # Incorrect password. 0 tries remaining.
    # Login unsucessful after 3 tries.
    # Unable to log in.
    # > login

    # Please input your username: danny

    # Please input your password: @my2Choices
    # Successfuly logged in. Welcome, danny.
    # > newuser

    # Please input your new username: danny
    # Invalid username. "danny" already exists.

    # Please input your new username: bob
    # Username accepted.

    # Please input your new password: hi
    # "hi" is an invalid password.
    # Password must contain at least one uppercase letter.
    # Password must contain at least one digit.
    # Password must contain at least one special character i.e. [@_!#$%^&*()<>?/\|}{~:]
    # Password must be at least eight characters long.

    # Please input your new password: Hi12345!
    # Password meets requirements.

    # Verify your password: ho
    # Passwords do not match. Please try again.

    # Please input your new password: Hi12345!
    # Password meets requirements.

    # Verify your password: Hi12345!
    # Welcome, bob.
    # > changepass

    # Please input your username: bob

    # Please input your password: hi
    # Incorrect password. 2 tries remaining.

    # Please input your password: ho
    # Incorrect password. 1 try remaining.

    # Please input your password: ha
    # Incorrect password. 0 tries remaining.
    # Login unsucessful after 3 tries.
    # Password change was unsuccessful.
    # > changepass

    # Please input your username: bob

    # Please input your password: Hi12345!

    # Please input your new password: Bye12345!
    # Password meets requirements.

    # Verify your password: Bye12345!
    # Password successfuly changed.
    # > q

    # Which task would you like to run? Type 1 or 2. Type q to quit: q



def task_two_main():
    try:
        file_one_name = input("Please input the name of the first file: ")
        file_one = open(file_one_name, "r", encoding = "utf-8-sig")
        file_two_name = input("Please input the name of the second file: ")
        file_two = open(file_two_name, "r", encoding = "utf-8-sig")
        file_one_list = get_list(file_one)
        print("Lines in {0}: {1}\nWords in {0}: {2}".format(file_one_name, file_one_list[1], file_one_list[2]))
        
        file_two_list = get_list(file_two)
        print("Lines in {0}: {1}\nWords in {0}: {2}".format(file_two_name, file_two_list[1], file_two_list[2]))

        file_one_set = get_set(file_one_list[0])
        file_two_set = get_set(file_two_list[0])

        union_set = file_one_set.union(file_two_set)
        print("\nThere are {0} total unique words in both files:\n{1}".format(len(union_set), union_set))
        one_not_two = file_one_set.difference(file_two_set)
        print("\nThere are {0} words in file one but not file two:\n{1}".format(len(one_not_two), one_not_two))
        two_not_one = file_two_set.difference(file_one_set)
        print("\nThere are {0} words in file two but not file one:\n{1}".format(len(two_not_one), two_not_one))
        intersection_set = file_one_set.intersection(file_two_set)
        print("\nThere are {0} words in both files:\n{1}".format(len(intersection_set), intersection_set))
        symm_diff_set = file_one_set.symmetric_difference(file_two_set)
        print("\nThere are {0} words in one file but not the other:\n{1}".format(len(symm_diff_set), symm_diff_set))

        freq_dict = get_freq(file_one_list[0] + file_two_list[0])
        print("\n\n")
        print(freq_dict)

        file_one.close()
        file_two.close()
    except FileNotFoundError:
        print("Unable to find file.")

def get_list(file):
    final_list = []
    lines = 0
    words = 0
    for line in file:
        line_final = []
        line = line.replace("-", " ")
        line = line.lower()
        line_split = line.split()
        for word in line_split:
            edited_word = ""
            for letter in word:
                if(letter.isalpha()):
                    edited_word += letter
            line_final.append(edited_word)
            words += 1
        final_list.append(line_final)
        lines += 1
    return final_list, lines, words
        
def get_set(list):
    final_set = set()
    for line in list:
        for word in line:
            final_set.add(word)
    return final_set

def get_freq(list):
    final_dict = {}
    for line in list:
        for word in line:
            if(not word in final_dict):
                final_dict[word] = 1
            else:
                final_dict[word] += 1
    final_dict = sorted(final_dict.items(), key = lambda x:x[1], reverse = True)
    return final_dict

    # TASK TWO OUTPUT:

    # Which task would you like to run? Type 1 or 2. Type q to quit: 2
    # Please input the name of the first file: Python.txt
    # Please input the name of the second file: MachineLearning.txt
    # Lines in Python.txt: 2
    # Words in Python.txt: 78
    # Lines in MachineLearning.txt: 1
    # Words in MachineLearning.txt: 50

    # There are 77 total unique words in both files:
    # {'improve', 'perform', 'specific', 'code', 'steps', 'ability', 'past', 'language', 'readability', 'languages', 'give', 'ranks', 'how', 'level', 'general', 'analyses', 'with', 'scikit', 'one', 'learns', 'to', 'statistical', 'and', 'will', 'of', 'get', 'experiences', 'application', 'step', 'philosophy', 'uses', 'that', 'dive', 'science', 'statistics', 'high', 'learn', 'from', 'data', 'they', 'popular', 'purpose', 'world', 'programming', 'a', 'making', 'intelligence', 'consistently', 'outcome', 'python', 'learning', 'you', 'library', 'predict', 'studying', 'necessary', 'using', 'computer', 'successful', 'program', 'techniques', 'is', 'the', 'create', 'ready', 'design', 'field', 'tasks', 'programs', 'into', 'by', 'most', 'as', 'machine', 'direction', 'artificial', 'emphasizes'}

    # There are 44 words in file one but not file two:
    # {'science', 'improve', 'high', 'perform', 'specific', 'they', 'popular', 'purpose', 'code', 'steps', 'programming', 'ability', 'past', 'language', 'readability', 'languages', 'give', 'ranks', 'consistently', 'how', 'level', 'library', 'you', 'general', 'with', 'necessary', 'scikit', 'one', 'successful', 'techniques', 'statistical', 'will', 'create', 'design', 'field', 'tasks', 'experiences', 'application', 'programs', 'most', 'philosophy', 'as', 'uses', 'emphasizes'}

    # There are 20 words in file two but not file one:
    # {'statistics', 'data', 'world', 'making', 'intelligence', 'outcome', 'predict', 'analyses', 'studying', 'using', 'learns', 'program', 'ready', 'get', 'step', 'into', 'by', 'direction', 'artificial', 'dive'}

    # There are 13 words in both files:
    # {'to', 'and', 'learn', 'is', 'from', 'the', 'python', 'learning', 'of', 'machine', 'that', 'a', 'computer'}

    # There are 64 words in one file but not the other:
    # {'science', 'improve', 'statistics', 'high', 'perform', 'specific', 'data', 'world', 'they', 'popular', 'purpose', 'code', 'steps', 'programming', 'ability', 'past', 'language', 'readability', 'making', 'intelligence', 'languages', 'give', 'ranks', 'consistently', 'outcome', 'how', 'emphasizes', 'level', 'predict', 'you', 'general', 'analyses', 'studying', 'library', 'with', 'necessary', 'learns', 'using', 'scikit', 'one', 'successful', 'program', 'techniques', 'statistical', 'will', 'create', 'ready', 'get', 'design', 'field', 'tasks', 'experiences', 'application', 'programs', 'step', 'into', 'by', 'most', 'philosophy', 'as', 'direction', 'uses', 'artificial', 'dive'}



    # [('the', 9), ('machine', 6), ('learning', 6), ('python', 5), ('is', 5), ('a', 5), ('of', 5), ('to', 5), ('learn', 4), ('and', 4), ('computer', 3), ('programming', 2), ('that', 2), ('from', 2), ('data', 2), ('into', 2), ('high', 1), ('level', 1), ('general', 1), ('purpose', 1), ('language', 1), ('design', 1), ('philosophy', 1), ('emphasizes', 1), ('code', 1), ('readability', 1), ('consistently', 1), ('ranks', 1), ('as', 1), ('one', 1), ('most', 1), ('popular', 1), ('languages', 1), ('field', 1), ('science', 1), ('uses', 1), ('statistical', 1), ('techniques', 1), ('give', 1), ('programs', 1), ('ability', 1), ('past', 1), ('experiences', 1), ('improve', 1), ('how', 1), ('they', 1), ('perform', 1), ('specific', 1), ('tasks', 1), ('you', 1), ('will', 1), ('steps', 1), ('necessary', 1), ('create', 1), ('successful', 1), ('application', 1), ('with', 1), ('scikit', 1), ('library', 1), ('making', 1), ('studying', 1), ('statistics', 1), ('step', 1), ('direction', 1), ('artificial', 1), ('intelligence', 1), ('program', 1), ('analyses', 1), ('learns', 1), ('predict', 1), ('outcome', 1), ('get', 1), ('ready', 1), ('dive', 1), ('world', 1), ('by', 1), ('using', 1)]

    # Which task would you like to run? Type 1 or 2. Type q to quit: 2
    # Please input the name of the first file: penguins.txt
    # Please input the name of the second file: turtles.txt
    # Lines in penguins.txt: 20
    # Words in penguins.txt: 451
    # Lines in turtles.txt: 21
    # Words in turtles.txt: 422

    # There are 391 total unique words in both files:
    # {'', 'modern', 'such', 'leatherback', 'flamboyant', 'tall', 'human', 'extreme', 'unfortunately', 'birds', 'teamwork', 'arctic', 'turns', 'eyes', 'activity', 'four', 'animated', 'padloper', 'feet', 'dandies', 'visitors', 'considered', 'excellent', 'with', 'australia', 'now', 'up', 'bony', 'females', 'include', 'ecosystem', 'face', 'sea', 'remarkable', 'hand', 'environments', 'krill', 'observe', 'eggs', 'together', 'change', 'listed', 'plastic', 'maneuver', 'years', 'your', 'flightless', 'lived', 'tortoise', 'deserts', 'hearts', 'turtle', 'deep', 'french', 'adapted', 'found', 'hemisphere', 'emperor', 'awareness', 'diving', 'iconic', 'symbols', 'ease', 'there', 'extensively', 'generations', 'beaches', 'diverse', 'luck', 'turtles', 'which', 'subzero', 'black', 'challenges', 'magnetic', 'scientific', 'reducing', 'wife', 'wisdom', 'breeding', 'wings', 'penguin', 'most', 'by', 'people', 'inability', 'million', 'acts', 'numbers', 'large', 'everything', 'continued', 'winds', 'pollution', 'keratin', 'adaptations', 'fit', 'imaginations', 'different', 'ability', 'can', 'overfishing', 'thrive', 'rockhopper', 'good', 'armor', 'specialized', 'ecosystems', 'like', 'antarctica', 'stands', 'decline', 'sports', 'working', 'significant', 'form', 'behavior', 'fly', 'tropics', 'water', 'their', 'threats', 'warm', 'survival', 'swimming', 'palm', 'saw', 'british', 'spiritual', 'anatomy', 'fascinating', 'worn', 'seen', 'changes', 'habitat', 'critical', 'role', 'for', 'africa', 'primarily', 'declining', 'penguins', 'or', 'just', 'back', 'new', 'climate', 'hope', 'world', 'while', 'opening', 'comical', 'due', 'yellow', 'bodies', 'usually', 'long', 'life', 'on', 'animals', 'century', 'species', 'many', 'history', 'during', 'often', 'material', 'using', 'depending', 'who', 'ensure', 'gets', 'zealand', 'survived', 'young', 'habitats', 'population', 'creatures', 'hair', 'where', 'adélie', 'symbol', 'parts', 'populations', 'gait', 'millions', 'white', 'african', 'help', 'efforts', 'example', 'th', 'inhabit', 'size', 'location', 'made', 'helps', 'them', 'effects', 'colonies', 'significance', 'caring', 'wetlands', 'protective', 'beliefs', 'fairy', 'loss', 'unique', 'be', 'makes', 'skin', 'king', 'ranging', 'and', 'icon', 'social', 'hats', 'offer', 'when', 'of', 'blooded', 'become', 'about', 'cold', 'wide', 'scutes', 'catch', 'captured', 'natural', 'squid', 'rookeries', 'important', 'vulnerable', 'we', 'variety', 'tufts', 'divers', 'work', 'withstand', 'plants', 'these', 'from', 'survive', 'they', 'popular', 'named', 'surface', 'after', 'environment', 'a', 'forests', 'season', 'earths', 'researchers', 'an', 'feeding', 'studying', 'first', 'swimmers', 'is', 'education', 'body', 'some', 'investigating', 'others', 'incubating', 'field', 'shell', 'continue', 'despite', 'part', 'hunting', 'known', 'feed', 'shells', 'more', 'studied', 'problems', 'spiky', 'name', 'crest', 'paddle', 'provides', 'threatened', 'tours', 'fish', 'absorb', 'waters', 'indicators', 'feathers', 'navigate', 'distinctive', 'find', 'take', 'below', 'waddling', 'watching', 'conclusion', 'tiny', 'head', 'incredibly', 'coloration', 'cultural', 'culture', 'resemble', 'over', 'nearly', 'come', 'endangered', 'covered', 'pounds', 'through', 'temperatures', 'highly', 'to', 'same', 'also', 'facing', 'adaptability', 'plates', 'buoyancy', 'have', 'quality', 'reduce', 'study', 'omnivorous', 'logos', 'weigh', 'longevity', 'scientists', 'including', 'oceans', 'harsh', 'speckled', 'degradation', 'way', 'that', 'southern', 'protect', 'nails', 'been', 'resilience', 'nesting', 'cloaca', 'beloved', 'macaroni', 'learn', 'able', 'notable', 'are', 'living', 'inches', 'streamlined', 'interested', 'in', 'south', 'males', 'subject', 'around', 'called', 'movies', 'mate', 'breathe', 'throughout', 'above', 'means', 'has', 'america', 'temperature', 'protecting', 'the', 'its', 'but', 'recent', 'adaptable', 'appearing', 'play', 'second', 'than', 'conservation', 'make', 'grow', 'explorer', 'reptiles', 'as', 'health', 'signify', 'largest', 'every', 'group', 'cultures'}

    # There are 180 words in file one but not file two:
    # {'modern', 'th', 'inhabit', 'flamboyant', 'tall', 'extreme', 'birds', 'african', 'teamwork', 'turns', 'eyes', 'activity', 'four', 'effects', 'animated', 'colonies', 'feet', 'dandies', 'caring', 'visitors', 'fairy', 'considered', 'excellent', 'australia', 'now', 'females', 'include', 'face', 'king', 'icon', 'hats', 'offer', 'social', 'become', 'about', 'krill', 'observe', 'eggs', 'change', 'catch', 'captured', 'natural', 'maneuver', 'squid', 'rookeries', 'flightless', 'tufts', 'work', 'divers', 'hearts', 'deep', 'french', 'adapted', 'withstand', 'hemisphere', 'these', 'survive', 'emperor', 'popular', 'awareness', 'diving', 'iconic', 'named', 'ease', 'surface', 'after', 'season', 'researchers', 'studying', 'first', 'subzero', 'black', 'challenges', 'swimmers', 'scientific', 'education', 'investigating', 'wife', 'incubating', 'breeding', 'despite', 'penguin', 'wings', 'most', 'people', 'inability', 'feed', 'numbers', 'spiky', 'name', 'crest', 'paddle', 'large', 'everything', 'tours', 'fish', 'continued', 'feathers', 'winds', 'imaginations', 'different', 'take', 'ability', 'below', 'waddling', 'watching', 'overfishing', 'rockhopper', 'head', 'coloration', 'culture', 'resemble', 'like', 'endangered', 'antarctica', 'stands', 'sports', 'temperatures', 'significant', 'highly', 'form', 'facing', 'fly', 'adaptability', 'saw', 'british', 'logos', 'worn', 'harsh', 'southern', 'africa', 'primarily', 'resilience', 'penguins', 'or', 'just', 'new', 'climate', 'hope', 'beloved', 'macaroni', 'learn', 'notable', 'comical', 'inches', 'streamlined', 'bodies', 'usually', 'yellow', 'life', 'south', 'century', 'during', 'often', 'males', 'movies', 'mate', 'gets', 'above', 'has', 'zealand', 'america', 'its', 'young', 'but', 'recent', 'appearing', 'creatures', 'second', 'grow', 'explorer', 'where', 'adélie', 'symbol', 'parts', 'largest', 'populations', 'gait', 'white', 'help'}

    # There are 136 words in file two but not file one:
    # {'leatherback', 'human', 'unfortunately', 'location', 'helps', 'arctic', 'padloper', 'significance', 'wetlands', 'protective', 'beliefs', 'be', 'bony', 'makes', 'ecosystem', 'skin', 'sea', 'remarkable', 'hand', 'when', 'blooded', 'cold', 'wide', 'scutes', 'listed', 'plastic', 'important', 'vulnerable', 'your', 'lived', 'variety', 'deserts', 'tortoise', 'turtle', 'plants', 'symbols', 'environment', 'forests', 'extensively', 'earths', 'feeding', 'beaches', 'diverse', 'luck', 'turtles', 'magnetic', 'body', 'reducing', 'others', 'field', 'shell', 'continue', 'wisdom', 'part', 'hunting', 'known', 'shells', 'studied', 'million', 'acts', 'problems', 'provides', 'threatened', 'absorb', 'waters', 'indicators', 'pollution', 'navigate', 'keratin', 'fit', 'find', 'good', 'incredibly', 'armor', 'cultural', 'specialized', 'over', 'nearly', 'covered', 'pounds', 'working', 'same', 'tropics', 'plates', 'warm', 'buoyancy', 'swimming', 'palm', 'quality', 'reduce', 'omnivorous', 'spiritual', 'anatomy', 'weigh', 'longevity', 'including', 'oceans', 'speckled', 'changes', 'degradation', 'critical', 'role', 'way', 'nails', 'declining', 'back', 'nesting', 'cloaca', 'able', 'opening', 'long', 'interested', 'history', 'material', 'called', 'using', 'depending', 'breathe', 'throughout', 'means', 'temperature', 'protecting', 'survived', 'habitats', 'population', 'adaptable', 'play', 'hair', 'than', 'make', 'reptiles', 'signify', 'health', 'every', 'millions', 'cultures'}

    # There are 75 words in both files:
    # {'', 'example', 'such', 'found', 'from', 'size', 'they', 'made', 'adaptations', 'distinctive', 'world', 'while', 'are', 'due', 'living', 'a', 'can', 'them', 'thrive', 'there', 'conclusion', 'tiny', 'in', 'on', 'an', 'animals', 'generations', 'species', 'many', 'come', 'loss', 'ecosystems', 'unique', 'with', 'around', 'subject', 'decline', 'through', 'up', 'which', 'who', 'ensure', 'to', 'also', 'ranging', 'and', 'behavior', 'is', 'their', 'water', 'of', 'some', 'survival', 'threats', 'have', 'the', 'environments', 'together', 'study', 'conservation', 'by', 'scientists', 'fascinating', 'seen', 'as', 'years', 'more', 'habitat', 'group', 'for', 'that', 'we', 'protect', 'been', 'efforts'}

    # There are 316 words in one file but not the other:
    # {'modern', 'human', 'teamwork', 'four', 'dandies', 'considered', 'now', 'ecosystem', 'include', 'remarkable', 'observe', 'change', 'lived', 'flightless', 'deserts', 'hearts', 'emperor', 'symbols', 'ease', 'extensively', 'beaches', 'diverse', 'luck', 'magnetic', 'black', 'people', 'wings', 'most', 'inability', 'million', 'acts', 'large', 'everything', 'continued', 'winds', 'pollution', 'fit', 'different', 'ability', 'rockhopper', 'good', 'armor', 'like', 'antarctica', 'sports', 'working', 'fly', 'tropics', 'warm', 'swimming', 'saw', 'role', 'back', 'or', 'just', 'new', 'hope', 'opening', 'yellow', 'bodies', 'usually', 'history', 'during', 'using', 'survived', 'habitats', 'population', 'where', 'adélie', 'populations', 'millions', 'th', 'helps', 'significance', 'beliefs', 'makes', 'skin', 'king', 'hats', 'icon', 'offer', 'social', 'become', 'wide', 'scutes', 'catch', 'captured', 'squid', 'vulnerable', 'tufts', 'survive', 'surface', 'season', 'researchers', 'feeding', 'first', 'body', 'others', 'field', 'shell', 'continue', 'part', 'hunting', 'known', 'feed', 'shells', 'problems', 'name', 'crest', 'paddle', 'waters', 'feathers', 'incredibly', 'head', 'cultural', 'over', 'culture', 'pounds', 'temperatures', 'highly', 'facing', 'adaptability', 'reduce', 'logos', 'weigh', 'longevity', 'oceans', 'speckled', 'degradation', 'southern', 'resilience', 'cloaca', 'able', 'beloved', 'macaroni', 'learn', 'notable', 'south', 'called', 'breathe', 'mate', 'throughout', 'above', 'america', 'recent', 'adaptable', 'appearing', 'second', 'than', 'make', 'reptiles', 'health', 'cultures', 'leatherback', 'flamboyant', 'tall', 'unfortunately', 'extreme', 'birds', 'arctic', 'turns', 'eyes', 'activity', 'animated', 'padloper', 'feet', 'visitors', 'excellent', 'australia', 'bony', 'females', 'face', 'sea', 'hand', 'krill', 'eggs', 'listed', 'plastic', 'maneuver', 'your', 'tortoise', 'turtle', 'deep', 'french', 'adapted', 'hemisphere', 'awareness', 'diving', 'iconic', 'turtles', 'subzero', 'challenges', 'scientific', 'reducing', 'wife', 'wisdom', 'breeding', 'penguin', 'numbers', 'keratin', 'imaginations', 'overfishing', 'specialized', 'stands', 'significant', 'form', 'palm', 'spiritual', 'anatomy', 'british', 'worn', 'changes', 'critical', 'africa', 'primarily', 'declining', 'penguins', 'climate', 'comical', 'long', 'life', 'century', 'often', 'material', 'depending', 'gets', 'zealand', 'young', 'creatures', 'hair', 'symbol', 'parts', 'gait', 'white', 'african', 'help', 'inhabit', 'location', 'effects', 'colonies', 'caring', 'wetlands', 'protective', 'fairy', 'be', 'when', 'blooded', 'about', 'cold', 'natural', 'important', 'rookeries', 'variety', 'divers', 'work', 'withstand', 'plants', 'these', 'popular', 'named', 'environment', 'after', 'forests', 'earths', 'studying', 'swimmers', 'education', 'investigating', 'incubating', 'despite', 'studied', 'spiky', 'provides', 'threatened', 'absorb', 'tours', 'fish', 'indicators', 'navigate', 'find', 'take', 'below', 'waddling', 'watching', 'coloration', 'nearly', 'resemble', 'endangered', 'covered', 'same', 'plates', 'buoyancy', 'quality', 'omnivorous', 'including', 'harsh', 'way', 'nails', 'nesting', 'inches', 'streamlined', 'interested', 'males', 'movies', 'means', 'temperature', 'protecting', 'has', 'its', 'but', 'play', 'grow', 'explorer', 'signify', 'largest', 'every'}



    # [('the', 41), ('and', 40), ('of', 29), ('are', 28), ('their', 28), ('in', 25), ('to', 22), ('turtles', 15), ('a', 13), ('for', 13), ('which', 12), ('species', 11), ('penguin', 11), ('penguins', 10), ('that', 9), ('also', 9), ('can', 9), ('have', 9), ('they', 7), ('', 7), ('many', 6), ('as', 6), ('water', 5), ('from', 5), ('them', 5), ('with', 5), ('on', 5), ('by', 5), ('world', 5), ('through', 4), ('animals', 4), ('years', 4), ('is', 4), ('some', 4), ('its', 4), ('been', 4), ('group', 3), ('found', 3), ('up', 3), ('habitat', 3), ('example', 3), ('popular', 3), ('fascinating', 3), ('subject', 3), ('unique', 3), ('adaptations', 3), ('more', 3), ('ecosystems', 3), ('conservation', 3), ('around', 3), ('sea', 3), ('turtle', 3), ('living', 2), ('primarily', 2), ('antarctica', 2), ('south', 2), ('there', 2), ('ranging', 2), ('size', 2), ('tiny', 2), ('tall', 2), ('emperor', 2), ('threats', 2), ('populations', 2), ('due', 2), ('loss', 2), ('climate', 2), ('change', 2), ('has', 2), ('seen', 2), ('decline', 2), ('an', 2), ('resilience', 2), ('adaptability', 2), ('distinctive', 2), ('behavior', 2), ('made', 2), ('beloved', 2), ('these', 2), ('creatures', 2), ('after', 2), ('feathers', 2), ('yellow', 2), ('who', 2), ('study', 2), ('environments', 2), ('such', 2), ('scientists', 2), ('while', 2), ('survival', 2), ('efforts', 2), ('we', 2), ('together', 2), ('protect', 2), ('ensure', 2), ('thrive', 2), ('generations', 2), ('come', 2), ('conclusion', 2), ('than', 2), ('waters', 2), ('cold', 2), ('leatherback', 2), ('over', 2), ('body', 2), ('temperature', 2), ('variety', 2), ('habitats', 2), ('cultural', 2), ('longevity', 2), ('pollution', 2), ('nesting', 2), ('beaches', 2), ('important', 2), ('able', 2), ('flightless', 1), ('birds', 1), ('highly', 1), ('adapted', 1), ('southern', 1), ('hemisphere', 1), ('but', 1), ('africa', 1), ('australia', 1), ('new', 1), ('zealand', 1), ('america', 1), ('different', 1), ('fairy', 1), ('stands', 1), ('just', 1), ('inches', 1), ('grow', 1), ('four', 1), ('feet', 1), ('despite', 1), ('inability', 1), ('fly', 1), ('excellent', 1), ('swimmers', 1), ('divers', 1), ('streamlined', 1), ('bodies', 1), ('paddle', 1), ('like', 1), ('wings', 1), ('help', 1), ('maneuver', 1), ('ease', 1), ('most', 1), ('feed', 1), ('fish', 1), ('squid', 1), ('krill', 1), ('catch', 1), ('diving', 1), ('deep', 1), ('below', 1), ('surface', 1), ('social', 1), ('often', 1), ('form', 1), ('large', 1), ('colonies', 1), ('or', 1), ('rookeries', 1), ('during', 1), ('breeding', 1), ('season', 1), ('males', 1), ('females', 1), ('usually', 1), ('mate', 1), ('life', 1), ('take', 1), ('turns', 1), ('incubating', 1), ('eggs', 1), ('caring', 1), ('young', 1), ('facing', 1), ('overfishing', 1), ('african', 1), ('significant', 1), ('numbers', 1), ('recent', 1), ('now', 1), ('considered', 1), ('endangered', 1), ('symbol', 1), ('teamwork', 1), ('black', 1), ('white', 1), ('coloration', 1), ('waddling', 1), ('gait', 1), ('comical', 1), ('icon', 1), ('culture', 1), ('appearing', 1), ('everything', 1), ('animated', 1), ('movies', 1), ('sports', 1), ('logos', 1), ('watching', 1), ('tours', 1), ('become', 1), ('activity', 1), ('parts', 1), ('where', 1), ('visitors', 1), ('observe', 1), ('natural', 1), ('notable', 1), ('include', 1), ('king', 1), ('second', 1), ('largest', 1), ('rockhopper', 1), ('spiky', 1), ('head', 1), ('tufts', 1), ('above', 1), ('eyes', 1), ('adélie', 1), ('named', 1), ('wife', 1), ('french', 1), ('explorer', 1), ('first', 1), ('saw', 1), ('macaroni', 1), ('gets', 1), ('name', 1), ('flamboyant', 1), ('crest', 1), ('resemble', 1), ('hats', 1), ('worn', 1), ('th', 1), ('century', 1), ('british', 1), ('dandies', 1), ('scientific', 1), ('researchers', 1), ('investigating', 1), ('extreme', 1), ('ability', 1), ('survive', 1), ('subzero', 1), ('temperatures', 1), ('withstand', 1), ('harsh', 1), ('winds', 1), ('studying', 1), ('learn', 1), ('about', 1), ('effects', 1), ('inhabit', 1), ('face', 1), ('challenges', 1), ('modern', 1), ('offer', 1), ('hope', 1), ('continued', 1), ('education', 1), ('awareness', 1), ('work', 1), ('iconic', 1), ('captured', 1), ('hearts', 1), ('imaginations', 1), ('people', 1), ('diverse', 1), ('reptiles', 1), ('million', 1), ('nearly', 1), ('every', 1), ('part', 1), ('warm', 1), ('tropics', 1), ('arctic', 1), ('speckled', 1), ('padloper', 1), ('tortoise', 1), ('fit', 1), ('palm', 1), ('your', 1), ('hand', 1), ('weigh', 1), ('pounds', 1), ('known', 1), ('shell', 1), ('acts', 1), ('protective', 1), ('armor', 1), ('provides', 1), ('buoyancy', 1), ('when', 1), ('swimming', 1), ('shells', 1), ('bony', 1), ('plates', 1), ('called', 1), ('scutes', 1), ('covered', 1), ('keratin', 1), ('same', 1), ('material', 1), ('makes', 1), ('human', 1), ('hair', 1), ('nails', 1), ('blooded', 1), ('means', 1), ('changes', 1), ('environment', 1), ('long', 1), ('lived', 1), ('incredibly', 1), ('adaptable', 1), ('be', 1), ('including', 1), ('deserts', 1), ('forests', 1), ('wetlands', 1), ('oceans', 1), ('omnivorous', 1), ('feeding', 1), ('wide', 1), ('plants', 1), ('depending', 1), ('location', 1), ('spiritual', 1), ('beliefs', 1), ('throughout', 1), ('history', 1), ('cultures', 1), ('symbols', 1), ('wisdom', 1), ('good', 1), ('luck', 1), ('unfortunately', 1), ('threatened', 1), ('hunting', 1), ('listed', 1), ('vulnerable', 1), ('declining', 1), ('population', 1), ('protecting', 1), ('reducing', 1), ('plastic', 1), ('critical', 1), ('indicators', 1), ('health', 1), ('signify', 1), ('problems', 1), ('quality', 1), ('ecosystem', 1), ('degradation', 1), ('studied', 1), ('extensively', 1), ('interested', 1), ('anatomy', 1), ('breathe', 1), ('skin', 1), ('others', 1), ('absorb', 1), ('cloaca', 1), ('specialized', 1), ('opening', 1), ('navigate', 1), ('using', 1), ('earths', 1), ('magnetic', 1), ('field', 1), ('helps', 1), ('find', 1), ('way', 1), ('back', 1), ('remarkable', 1), ('survived', 1), ('millions', 1), ('play', 1), ('role', 1), ('significance', 1), ('make', 1), ('working', 1), ('reduce', 1), ('continue', 1)]

    # Which task would you like to run? Type 1 or 2. Type q to quit: q


# Task selector
while(True):
    try:
        selection = input("Which task would you like to run? Type 1 or 2. Type q to quit: ")
        if (selection == "q"):
            quit()
        if (int(selection) == 1):
            task_one_main()
        elif (int(selection) == 2):
            task_two_main()
    except ValueError:
        print("Invalid input.")
    print()