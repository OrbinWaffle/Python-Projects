# Name: Joshua Lai
# Project 3
# Completed 4/17/2022

from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
        print("\n")
        print(freq_dict)

        file_one.close()
        file_two.close()

        generate_wordcloud(freq_dict)
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
            if(len(edited_word) > 0):
                line_final.append(edited_word)
            words += 1
        if(len(line_final) > 0):
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
    return dict(final_dict)

def generate_wordcloud(dictionary):
    wordcloud = WordCloud().generate_from_frequencies(dictionary)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # TASK TWO OUTPUT:

    # Which task would you like to run? Type 1 or 2. Type q to quit: 2
    # Please input the name of the first file: Python.txt
    # Please input the name of the second file: MachineLearning.txt
    # Lines in Python.txt: 2
    # Words in Python.txt: 78
    # Lines in MachineLearning.txt: 1
    # Words in MachineLearning.txt: 50

    # There are 77 total unique words in both files:
    # {'world', 'intelligence', 'high', 'popular', 'readability', 'from', 'most', 'experiences', 'they', 'necessary', 'outcome', 'ranks', 'with', 'will', 'ability', 'specific', 'successful', 'dive', 'direction', 'a', 'data', 'learning', 'using', 'by', 'as', 'learns', 'programming', 'studying', 'to', 'steps', 'perform', 'that', 'program', 'give', 'the', 'step', 'statistics', 'level', 'field', 'is', 'you', 'improve', 'emphasizes', 'learn', 'machine', 'one', 'ready', 'how', 'past', 'library', 'analyses', 'science', 'general', 'computer', 'purpose', 'scikit', 'languages', 'statistical', 'techniques', 'design', 'code', 'tasks', 'application', 'python', 'create', 'predict', 'into', 'language', 'artificial', 'philosophy', 'uses', 'consistently', 'and', 'of', 'programs', 'get', 'making'}

    # There are 44 words in file one but not file two:
    # {'high', 'popular', 'readability', 'past', 'most', 'experiences', 'how', 'they', 'library', 'science', 'general', 'necessary', 'purpose', 'scikit', 'languages', 'ranks', 'statistical', 'techniques', 'with', 'design', 'will', 'ability', 'code', 'specific', 'tasks', 'successful', 'application', 'as', 'programming', 'steps', 'create', 'perform', 'language', 'philosophy', 'give', 'uses', 'level', 'field', 'consistently', 'programs', 'you', 'improve', 'emphasizes', 'one'}

    # There are 20 words in file two but not file one:
    # {'ready', 'world', 'intelligence', 'analyses', 'outcome', 'dive', 'direction', 'data', 'using', 'by', 'learns', 'studying', 'predict', 'into', 'artificial', 'program', 'step', 'statistics', 'get', 'making'}

    # There are 13 words in both files:
    # {'the', 'python', 'from', 'is', 'and', 'of', 'to', 'that', 'a', 'computer', 'learning', 'learn', 'machine'}

    # There are 64 words in one file but not the other:
    # {'ready', 'world', 'intelligence', 'high', 'popular', 'experiences', 'readability', 'analyses', 'most', 'past', 'how', 'they', 'library', 'science', 'general', 'necessary', 'purpose', 'scikit', 'outcome', 'languages', 'ranks', 'statistical', 'techniques', 'with', 'design', 'will', 'ability', 'code', 'specific', 'tasks', 'dive', 'successful', 'direction', 'data', 'application', 'using', 'by', 'as', 'learns', 'studying', 'programming', 'predict', 'into', 'steps', 'create', 'perform', 'language', 'artificial', 'philosophy', 'program', 'give', 'step', 'statistics', 'uses', 'level', 'field', 'consistently', 'programs', 'you', 'improve', 'get', 'emphasizes', 'making', 'one'}


    # {'the': 9, 'machine': 6, 'learning': 6, 'python': 5, 'is': 5, 'a': 5, 'of': 5, 'to': 5, 'learn': 4, 'and': 4, 'computer': 3, 'programming': 2, 'that': 2, 'from': 2, 'data': 2, 'into': 2, 'high': 1, 'level': 1, 'general': 1, 'purpose': 1, 'language': 1, 'design': 1, 'philosophy': 1, 'emphasizes': 1, 'code': 1, 'readability': 1, 'consistently': 1, 'ranks': 1, 'as': 1, 'one': 1, 'most': 1, 'popular': 1, 'languages': 1, 'field': 1, 'science': 1, 'uses': 1, 'statistical': 1, 'techniques': 1, 'give': 1, 'programs': 1, 'ability': 1, 'past': 1, 'experiences': 1, 'improve': 1, 'how': 1, 'they': 1, 'perform': 1, 'specific': 1, 'tasks': 1, 'you': 1, 'will': 1, 'steps': 1, 'necessary': 1, 'create': 1, 'successful': 1, 'application': 1, 'with': 1, 'scikit': 1, 'library': 1, 'making': 1, 'studying': 1, 'statistics': 1, 'step': 1, 'direction': 1, 'artificial': 1, 'intelligence': 1, 'program': 1, 'analyses': 1, 'learns': 1, 'predict': 1, 'outcome': 1, 'get': 1, 'ready': 1, 'dive': 1, 'world': 1, 'by': 1, 'using': 1}

    # Which task would you like to run? Type 1 or 2. Type q to quit: 2
    # Please input the name of the first file: penguins.txt
    # Please input the name of the second file: turtles.txt
    # Lines in penguins.txt: 20
    # Words in penguins.txt: 451
    # Lines in turtles.txt: 21
    # Words in turtles.txt: 422

    # There are 390 total unique words in both files:
    # {'remarkable', 'water', 'watching', 'from', 'logos', 'cloaca', 'southern', 'harsh', 'threatened', 'over', 'investigating', 'warm', 'spiritual', 'south', 'cold', 'shells', 'swimming', 'ease', 'its', 'everything', 'them', 'vulnerable', 'using', 'waters', 'th', 'saw', 'social', 'as', 'nesting', 'explorer', 'been', 'species', 'inability', 'back', 'icon', 'conservation', 'tall', 'recent', 'facing', 'black', 'habitats', 'come', 'beloved', 'plates', 'studied', 'america', 'squid', 'is', 'field', 'parts', 'largest', 'degradation', 'survived', 'rookeries', 'hope', 'inches', 'seen', 'effects', 'habitat', 'role', 'ensure', 'shell', 'more', 'coloration', 'highly', 'dandies', 'efforts', 'macaroni', 'grow', 'iconic', 'include', 'specialized', 'tufts', 'provides', 'captured', 'century', 'speckled', 'symbols', 'education', 'four', 'protect', 'name', 'way', 'means', 'on', 'primarily', 'excellent', 'wife', 'gets', 'just', 'overfishing', 'french', 'deep', 'nearly', 'critical', 'breathe', 'play', 'arctic', 'make', 'sports', 'but', 'keratin', 'form', 'beaches', 'and', 'australia', 'palm', 'material', 'change', 'world', 'significant', 'culture', 'during', 'feeding', 'up', 'flightless', 'made', 'activity', 'blooded', 'adélie', 'considered', 'penguins', 'good', 'cultures', 'decline', 'resemble', 'adaptations', 'antarctica', 'bodies', 'due', 'feathers', 'including', 'resilience', 'inhabit', 'often', 'by', 'like', 'anatomy', 'modern', 'notable', 'has', 'nails', 'studying', 'to', 'spiky', 'colonies', 'turns', 'survive', 'are', 'populations', 'white', 'named', 'different', 'females', 'able', 'tiny', 'the', 'pollution', 'plants', 'teamwork', 'absorb', 'there', 'living', 'subject', 'skin', 'adapted', 'or', 'temperatures', 'about', 'acts', 'hair', 'opening', 'environment', 'work', 'population', 'padloper', 'beliefs', 'lived', 'significance', 'flamboyant', 'fish', 'face', 'incredibly', 'krill', 'reducing', 'earths', 'navigate', 'fairy', 'for', 'gait', 'pounds', 'symbol', 'surface', 'streamlined', 'many', 'behavior', 'appearing', 'be', 'scutes', 'of', 'divers', 'extreme', 'example', 'survival', 'threats', 'depending', 'armor', 'environments', 'million', 'unique', 'birds', 'second', 'omnivorous', 'temperature', 'protecting', 'years', 'movies', 'emperor', 'hand', 'where', 'endangered', 'wings', 'plastic', 'listed', 'around', 'sea', 'tortoise', 'help', 'despite', 'known', 'than', 'luck', 'hearts', 'protective', 'season', 'helps', 'find', 'buoyancy', 'wetlands', 'health', 'visitors', 'diving', 'people', 'extensively', 'awareness', 'diverse', 'reduce', 'comical', 'we', 'cultural', 'hemisphere', 'while', 'important', 'signify', 'africa', 'group', 'in', 'same', 'throughout', 'generations', 'human', 'below', 'life', 'problems', 'crest', 'deserts', 'also', 'withstand', 'hats', 'fascinating', 'yellow', 'body', 'ecosystems', 'millions', 'ranging', 'take', 'head', 'become', 'continued', 'makes', 'turtles', 'such', 'subzero', 'your', 'who', 'continue', 'numbers', 'bony', 'penguin', 'oceans', 'their', 'incubating', 'maneuver', 'quality', 'scientists', 'popular', 'most', 'they', 'ecosystem', 'new', 'fly', 'young', 'wide', 'turtle', 'others', 'conclusion', 'challenges', 'with', 'animated', 'study', 'british', 'stands', 'ability', 'paddle', 'males', 'a', 'eggs', 'zealand', 'animals', 'fit', 'rockhopper', 'after', 'thrive', 'offer', 'which', 'that', 'indicators', 'reptiles', 'winds', 'adaptability', 'found', 'king', 'eyes', 'declining', 'imaginations', 'changes', 'adaptable', 'through', 'observe', 'feed', 'these', 'an', 'covered', 'loss', 'swimmers', 'learn', 'large', 'now', 'worn', 'leatherback', 'climate', 'creatures', 'long', 'tours', 'catch', 'some', 'hunting', 'forests', 'interested', 'waddling', 'magnetic', 'part', 'called', 'first', 'history', 'can', 'tropics', 'weigh', 'usually', 'have', 'wisdom', 'distinctive', 'unfortunately', 'size', 'breeding', 'caring', 'variety', 'african', 'together', 'every', 'above', 'mate', 'location', 'scientific', 'feet', 'when', 'researchers', 'working', 'longevity', 'natural'}

    # There are 180 words in file one but not file two:
    # {'watching', 'birds', 'second', 'logos', 'movies', 'southern', 'emperor', 'harsh', 'investigating', 'where', 'endangered', 'south', 'wings', 'ease', 'its', 'everything', 'help', 'despite', 'hearts', 'season', 'th', 'saw', 'social', 'explorer', 'visitors', 'diving', 'people', 'inability', 'awareness', 'icon', 'tall', 'recent', 'facing', 'black', 'comical', 'beloved', 'hemisphere', 'america', 'squid', 'parts', 'africa', 'largest', 'rookeries', 'hope', 'inches', 'effects', 'below', 'coloration', 'life', 'highly', 'dandies', 'macaroni', 'grow', 'crest', 'iconic', 'include', 'withstand', 'tufts', 'hats', 'captured', 'yellow', 'century', 'education', 'four', 'name', 'primarily', 'excellent', 'wife', 'gets', 'just', 'take', 'overfishing', 'french', 'deep', 'head', 'become', 'continued', 'sports', 'but', 'subzero', 'form', 'australia', 'numbers', 'penguin', 'incubating', 'change', 'maneuver', 'significant', 'culture', 'during', 'popular', 'most', 'flightless', 'new', 'activity', 'fly', 'young', 'adélie', 'considered', 'challenges', 'animated', 'penguins', 'british', 'stands', 'resemble', 'ability', 'paddle', 'antarctica', 'bodies', 'males', 'feathers', 'eggs', 'resilience', 'often', 'inhabit', 'zealand', 'like', 'modern', 'notable', 'has', 'after', 'rockhopper', 'studying', 'offer', 'spiky', 'colonies', 'turns', 'survive', 'populations', 'white', 'named', 'different', 'females', 'winds', 'adaptability', 'king', 'eyes', 'imaginations', 'observe', 'feed', 'teamwork', 'these', 'swimmers', 'learn', 'large', 'now', 'worn', 'adapted', 'climate', 'creatures', 'or', 'tours', 'catch', 'temperatures', 'about', 'waddling', 'first', 'work', 'flamboyant', 'usually', 'fish', 'face', 'krill', 'fairy', 'breeding', 'caring', 'african', 'gait', 'symbol', 'above', 'mate', 'surface', 'streamlined', 'scientific', 'feet', 'appearing', 'divers', 'researchers', 'extreme', 'natural'}

    # There are 136 words in file two but not file one:
    # {'remarkable', 'omnivorous', 'cloaca', 'protecting', 'temperature', 'threatened', 'over', 'warm', 'hand', 'spiritual', 'cold', 'shells', 'plastic', 'swimming', 'listed', 'sea', 'tortoise', 'known', 'than', 'luck', 'vulnerable', 'using', 'waters', 'protective', 'helps', 'find', 'buoyancy', 'wetlands', 'nesting', 'health', 'extensively', 'back', 'diverse', 'reduce', 'habitats', 'cultural', 'plates', 'studied', 'field', 'important', 'signify', 'survived', 'degradation', 'same', 'throughout', 'role', 'shell', 'human', 'problems', 'deserts', 'specialized', 'provides', 'speckled', 'symbols', 'body', 'way', 'means', 'millions', 'nearly', 'critical', 'breathe', 'play', 'arctic', 'turtles', 'makes', 'make', 'your', 'keratin', 'beaches', 'palm', 'continue', 'material', 'bony', 'oceans', 'quality', 'feeding', 'ecosystem', 'blooded', 'wide', 'turtle', 'others', 'good', 'cultures', 'including', 'anatomy', 'fit', 'nails', 'indicators', 'reptiles', 'able', 'declining', 'changes', 'adaptable', 'plants', 'pollution', 'covered', 'absorb', 'leatherback', 'skin', 'long', 'hunting', 'acts', 'forests', 'hair', 'interested', 'opening', 'environment', 'magnetic', 'part', 'called', 'history', 'population', 'padloper', 'beliefs', 'tropics', 'lived', 'weigh', 'significance', 'wisdom', 'incredibly', 'reducing', 'unfortunately', 'earths', 'navigate', 'variety', 'every', 'pounds', 'location', 'be', 'when', 'scutes', 'working', 'longevity', 'depending', 'armor', 'million'}

    # There are 74 words in both files:
    # {'water', 'world', 'unique', 'group', 'in', 'from', 'seen', 'habitat', 'years', 'generations', 'scientists', 'ensure', 'they', 'made', 'up', 'more', 'efforts', 'can', 'conclusion', 'also', 'with', 'around', 'study', 'decline', 'fascinating', 'adaptations', 'them', 'have', 'due', 'distinctive', 'ecosystems', 'protect', 'a', 'by', 'on', 'size', 'animals', 'some', 'for', 'as', 'together', 'ranging', 'thrive', 'been', 'species', 'to', 'which', 'conservation', 'are', 'many', 'that', 'behavior', 'we', 'such', 'tiny', 'found', 'the', 'come', 'through', 'while', 'is', 'and', 'of', 'who', 'an', 'example', 'survival', 'threats', 'loss', 'there', 'environments', 'living', 'subject', 'their'}

    # There are 316 words in one file but not the other:
    # {'threatened', 'southern', 'over', 'warm', 'south', 'cold', 'shells', 'swimming', 'ease', 'vulnerable', 'saw', 'nesting', 'explorer', 'back', 'icon', 'tall', 'recent', 'facing', 'habitats', 'black', 'largest', 'degradation', 'survived', 'hope', 'effects', 'shell', 'coloration', 'highly', 'iconic', 'tufts', 'captured', 'century', 'education', 'four', 'primarily', 'excellent', 'wife', 'overfishing', 'deep', 'nearly', 'breathe', 'arctic', 'make', 'sports', 'but', 'form', 'beaches', 'change', 'feeding', 'flightless', 'blooded', 'good', 'resemble', 'including', 'antarctica', 'feathers', 'often', 'like', 'modern', 'notable', 'nails', 'studying', 'colonies', 'populations', 'different', 'able', 'females', 'pollution', 'teamwork', 'skin', 'adapted', 'acts', 'environment', 'beliefs', 'significance', 'flamboyant', 'face', 'incredibly', 'krill', 'reducing', 'navigate', 'pounds', 'symbol', 'surface', 'appearing', 'scutes', 'birds', 'movies', 'hand', 'where', 'endangered', 'tortoise', 'help', 'known', 'luck', 'hearts', 'protective', 'wetlands', 'health', 'awareness', 'diverse', 'reduce', 'comical', 'cultural', 'important', 'signify', 'africa', 'below', 'crest', 'deserts', 'hats', 'take', 'head', 'become', 'makes', 'turtles', 'subzero', 'incubating', 'maneuver', 'ecosystem', 'young', 'challenges', 'males', 'fit', 'offer', 'declining', 'winds', 'adaptable', 'observe', 'feed', 'these', 'covered', 'leatherback', 'long', 'tours', 'hunting', 'interested', 'magnetic', 'part', 'called', 'history', 'tropics', 'wisdom', 'breeding', 'variety', 'caring', 'every', 'location', 'scientific', 'working', 'researchers', 'natural', 'remarkable', 'watching', 'logos', 'cloaca', 'harsh', 'investigating', 'spiritual', 'its', 'everything', 'using', 'waters', 'th', 'social', 'inability', 'plates', 'beloved', 'studied', 'america', 'field', 'squid', 'parts', 'rookeries', 'inches', 'role', 'dandies', 'macaroni', 'grow', 'include', 'specialized', 'provides', 'speckled', 'symbols', 'name', 'way', 'means', 'gets', 'just', 'french', 'critical', 'play', 'keratin', 'palm', 'australia', 'material', 'significant', 'culture', 'during', 'activity', 'adélie', 'considered', 'penguins', 'cultures', 'bodies', 'resilience', 'inhabit', 'anatomy', 'has', 'spiky', 'turns', 'survive', 'named', 'white', 'plants', 'absorb', 'or', 'temperatures', 'about', 'hair', 'opening', 'work', 'population', 'padloper', 'lived', 'fish', 'earths', 'fairy', 'gait', 'streamlined', 'be', 'divers', 'extreme', 'depending', 'armor', 'million', 'omnivorous', 'second', 'temperature', 'protecting', 'emperor', 'wings', 'plastic', 'listed', 'sea', 'despite', 'than', 'season', 'helps', 'find', 'buoyancy', 'visitors', 'diving', 'people', 'extensively', 'hemisphere', 'same', 'throughout', 'human', 'life', 'problems', 'withstand', 'yellow', 'body', 'millions', 'continued', 'your', 'continue', 'numbers', 'bony', 'oceans', 'penguin', 'quality', 'popular', 'most', 'new', 'fly', 'wide', 'turtle', 'others', 'animated', 'british', 'stands', 'ability', 'paddle', 'eggs', 'zealand', 'rockhopper', 'after', 'indicators', 'reptiles', 'adaptability', 'king', 'eyes', 'changes', 'imaginations', 'swimmers', 'learn', 'large', 'now', 'worn', 'climate', 'creatures', 'catch', 'forests', 'waddling', 'first', 'weigh', 'usually', 'unfortunately', 'african', 'above', 'mate', 'feet', 'when', 'longevity'}


    # {'the': 41, 'and': 40, 'of': 29, 'are': 28, 'their': 28, 'in': 25, 'to': 22, 'turtles': 15, 'a': 13, 'for': 13, 'which': 12, 'species': 11, 'penguin': 11, 'penguins': 10, 'that': 9, 'also': 9, 'can': 9, 'have': 9, 'they': 7, 'many': 6, 'as': 6, 'water': 5, 'from': 5, 'them': 5, 'with': 5, 'on': 5, 'by': 5, 'world': 5, 'through': 4, 'animals': 4, 'years': 4, 'is': 4, 'some': 4, 'its': 4, 'been': 4, 'group': 3, 'found': 3, 'up': 3, 'habitat': 3, 'example': 3, 'popular': 3, 'fascinating': 3, 'subject': 3, 'unique': 3, 'adaptations': 3, 'more': 3, 'ecosystems': 3, 'conservation': 3, 'around': 3, 'sea': 3, 'turtle': 3, 'living': 2, 'primarily': 2, 'antarctica': 2, 'south': 2, 'there': 2, 'ranging': 2, 'size': 2, 'tiny': 2, 'tall': 2, 'emperor': 2, 'threats': 2, 'populations': 2, 'due': 2, 'loss': 2, 'climate': 2, 'change': 2, 'has': 2, 'seen': 2, 'decline': 2, 'an': 2, 'resilience': 2, 'adaptability': 2, 'distinctive': 2, 'behavior': 2, 'made': 2, 'beloved': 2, 'these': 2, 'creatures': 2, 'after': 2, 'feathers': 2, 'yellow': 2, 'who': 2, 'study': 2, 'environments': 2, 'such': 2, 'scientists': 2, 'while': 2, 'survival': 2, 'efforts': 2, 'we': 2, 'together': 2, 'protect': 2, 'ensure': 2, 'thrive': 2, 'generations': 2, 'come': 2, 'conclusion': 2, 'than': 2, 'waters': 2, 'cold': 2, 'leatherback': 2, 'over': 2, 'body': 2, 'temperature': 2, 'variety': 2, 'habitats': 2, 'cultural': 2, 'longevity': 2, 'pollution': 2, 'nesting': 2, 'beaches': 2, 'important': 2, 'able': 2, 'flightless': 1, 'birds': 1, 'highly': 1, 'adapted': 1, 'southern': 1, 'hemisphere': 1, 'but': 1, 'africa': 1, 'australia': 1, 'new': 1, 'zealand': 1, 'america': 1, 'different': 1, 'fairy': 1, 'stands': 1, 'just': 1, 'inches': 1, 'grow': 1, 'four': 1, 'feet': 1, 'despite': 1, 'inability': 1, 'fly': 1, 'excellent': 1, 'swimmers': 1, 'divers': 1, 'streamlined': 1, 'bodies': 1, 'paddle': 1, 'like': 1, 'wings': 1, 'help': 1, 'maneuver': 1, 'ease': 1, 'most': 1, 'feed': 1, 'fish': 1, 'squid': 1, 'krill': 1, 'catch': 1, 'diving': 1, 'deep': 1, 'below': 1, 'surface': 1, 'social': 1, 'often': 1, 'form': 1, 'large': 1, 'colonies': 1, 'or': 1, 'rookeries': 1, 'during': 1, 'breeding': 1, 'season': 1, 'males': 1, 'females': 1, 'usually': 1, 'mate': 1, 'life': 1, 'take': 1, 'turns': 1, 'incubating': 1, 'eggs': 1, 'caring': 1, 'young': 1, 'facing': 1, 'overfishing': 1, 'african': 1, 'significant': 1, 'numbers': 1, 'recent': 1, 'now': 1, 'considered': 1, 'endangered': 1, 'symbol': 1, 'teamwork': 1, 'black': 1, 'white': 1, 'coloration': 1, 'waddling': 1, 'gait': 1, 'comical': 1, 'icon': 1, 'culture': 1, 'appearing': 1, 'everything': 1, 'animated': 1, 'movies': 1, 'sports': 1, 'logos': 1, 'watching': 1, 'tours': 1, 'become': 1, 'activity': 1, 'parts': 1, 'where': 1, 'visitors': 1, 'observe': 1, 'natural': 1, 'notable': 1, 'include': 1, 'king': 1, 'second': 1, 'largest': 1, 'rockhopper': 1, 'spiky': 1, 'head': 1, 'tufts': 1, 'above': 1, 'eyes': 1, 'adélie': 1, 'named': 1, 'wife': 1, 'french': 1, 'explorer': 1, 'first': 1, 'saw': 1, 'macaroni': 1, 'gets': 1, 'name': 1, 'flamboyant': 1, 'crest': 1, 'resemble': 1, 'hats': 1, 'worn': 1, 'th': 1, 'century': 1, 'british': 1, 'dandies': 1, 'scientific': 1, 'researchers': 1, 'investigating': 1, 'extreme': 1, 'ability': 1, 'survive': 1, 'subzero': 1, 'temperatures': 1, 'withstand': 1, 'harsh': 1, 'winds': 1, 'studying': 1, 'learn': 1, 'about': 1, 'effects': 1, 'inhabit': 1, 'face': 1, 'challenges': 1, 'modern': 1, 'offer': 1, 'hope': 1, 'continued': 1, 'education': 1, 'awareness': 1, 'work': 1, 'iconic': 1, 'captured': 1, 'hearts': 1, 'imaginations': 1, 'people': 1, 'diverse': 1, 'reptiles': 1, 'million': 1, 'nearly': 1, 'every': 1, 'part': 1, 'warm': 1, 'tropics': 1, 'arctic': 1, 'speckled': 1, 'padloper': 1, 'tortoise': 1, 'fit': 1, 'palm': 1, 'your': 1, 'hand': 1, 'weigh': 1, 'pounds': 1, 'known': 1, 'shell': 1, 'acts': 1, 'protective': 1, 'armor': 1, 'provides': 1, 'buoyancy': 1, 'when': 1, 'swimming': 1, 'shells': 1, 'bony': 1, 'plates': 1, 'called': 1, 'scutes': 1, 'covered': 1, 'keratin': 1, 'same': 1, 'material': 1, 'makes': 1, 'human': 1, 'hair': 1, 'nails': 1, 'blooded': 1, 'means': 1, 'changes': 1, 'environment': 1, 'long': 1, 'lived': 1, 'incredibly': 1, 'adaptable': 1, 'be': 1, 'including': 1, 'deserts': 1, 'forests': 1, 'wetlands': 1, 'oceans': 1, 'omnivorous': 1, 'feeding': 1, 'wide': 1, 'plants': 1, 'depending': 1, 'location': 1, 'spiritual': 1, 'beliefs': 1, 'throughout': 1, 'history': 1, 'cultures': 1, 'symbols': 1, 'wisdom': 1, 'good': 1, 'luck': 1, 'unfortunately': 1, 'threatened': 1, 'hunting': 1, 'listed': 1, 'vulnerable': 1, 'declining': 1, 'population': 1, 'protecting': 1, 'reducing': 1, 'plastic': 1, 'critical': 1, 'indicators': 1, 'health': 1, 'signify': 1, 'problems': 1, 'quality': 1, 'ecosystem': 1, 'degradation': 1, 'studied': 1, 'extensively': 1, 'interested': 1, 'anatomy': 1, 'breathe': 1, 'skin': 1, 'others': 1, 'absorb': 1, 'cloaca': 1, 'specialized': 1, 'opening': 1, 'navigate': 1, 'using': 1, 'earths': 1, 'magnetic': 1, 'field': 1, 'helps': 1, 'find': 1, 'way': 1, 'back': 1, 'remarkable': 1, 'survived': 1, 'millions': 1, 'play': 1, 'role': 1, 'significance': 1, 'make': 1, 'working': 1, 'reduce': 1, 'continue': 1}

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