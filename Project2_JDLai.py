# Name: Joshua Lai
# Project 2
# Completed 3/7/2022

import time
from turtle import Turtle, Screen

def task_one_main():
    user_input = input("Enter a sentence: ")
    encryption_key = input("Enter an encryption key: ")
    num_of_chars = get_num_of_characters(user_input)
    no_whitespace = output_without_whitespace(user_input)
    encrypted = get_safe(user_input, encryption_key)
    decrypted = go_recover(encrypted, encryption_key)
    print("Your sentence:", user_input)
    print("This sentence has {0} characters.".format(num_of_chars))
    print("Without whitespace, your sentence is:", no_whitespace)
    print("Your sentence encrypted is:", encrypted)
    print("Your sentence decryped is:", decrypted)
    return
    

def get_num_of_characters(input_string):
    count = 0
    for character in input_string:
        count += 1
    return count

def output_without_whitespace(input_string):
    result = input_string
    result = result.replace(" ", "")
    result = result.replace("\t", "")
    return result
def get_safe(input_string, key):
    # get string lengths
    string_length = len(input_string)
    key_length = len(key)
    for i in range(string_length):
        # get unicode values
        character = ord(input_string[i])
        keyChar = ord(key[i%key_length])
        # xor values together and turn back to character
        result_char = chr(character ^ keyChar)
        input_string = input_string[:i] + result_char + input_string[(i+1):]
    return input_string

# because the xor cipher works both ways, the decryption method
# is identical to the encryption one.
def go_recover(input_string, key):
    return get_safe(input_string, key)

# TASK ONE OUTPUT:
# Which task would you like to run? Type 1, 2, or 3: 1
# Enter a sentence: The only thing we have to fear is fear itself.
# Your sentence: The only thing we have to fear is fear itself.
# This sentence has 46 characters.
# Without whitespace, your sentence is: Theonlythingwehavetofearisfearitself.
# Your sentence encrypted is: ▼☺◄T
# ☼♣.▬*↔▬N§♠T♀→.♣↕Z
# Your sentence decryped is: The only thing we have to fear is fear itself.

# Which task would you like to run? Type 1, 2, or 3: 1
# Enter an encryption key: William
# Your sentence: To be, or not to be, that is the question.
# This sentence has 42 characters.
# Without whitespace, your sentence is: Tobe,ornottobe,thatisthequestion.
# ↑▲w↔♦senI►↑2→↑♣♠☼Cypted is: ♥♠L♫♀MM8☻♠§M#♠L♫♀MM#☺
# Your sentence decryped is: To be, or not to be, that is the question.

# Which task would you like to run? Type 1, 2, or 3: 1
# Enter a sentence: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
# Enter an encryption key: snake     
# Your sentence: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
# This sentence has 98 characters.
# Without whitespace, your sentence is: Pythonisaninterpreted,object-oriented,high-levelprogramminglanguagewithdynamicsemantics.
# Your sentence encrypted is: #↨§♥
# K§☺☺♠↓♦▲♣☻S☻♣☻♠☼♠♫E♦§♥E↨↨☼☼▼↨BA♥♀¶♠L♣♂
# A↑▲☼☼▼♀►↔O
# Your sentence decryped is: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.



def task_two_main():
    prime_generator = generate_primes(1100)
    print("First 50 prime numbers: ")
    # generate 50 primes
    for i in range(50):
        print(next(prime_generator), end = " ")
    print()
    # skip 50 primes
    for i in range(50):
        next(prime_generator)
    
    startTIme = time.time()
    # generate 101st prime
    print("101st prime number:", next(prime_generator))
    # skip 998 primes
    for i in range(998):
        next(prime_generator)
    # generate 1001st prime
    print("1001st prime number:", next(prime_generator))
    endTime = time.time()
    totalTime = endTime - startTIme
    print("It took {0} seconds to run step two.".format(totalTime))
        
def generate_primes(num_of_primes):
    primes_generated = 0
    index = 2
    while(primes_generated < num_of_primes):
        num_to_add = index
        # iterate over every value up to this index.
        # if we can divide by one of these values, this number is not prime.
        for i in range(2, index):
            if(num_to_add % i == 0):
                break
        else:
            primes_generated += 1
            yield num_to_add
        index += 1

# TASK TWO OUTPUT:
# Which task would you like to run? Type 1, 2, or 3: 2
# First 50 prime numbers: 
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229
# 101st prime number: 547
# 1001st prime number: 8831
# It took 0.1860487461090088 seconds to run step two.



def task_three_main():
    zip_code = input("Please enter your zip code: ")
    generate_bar_code(zip_code)

codes = ["11000", "00011", "00101", "00110", "01001", "01010", "01100", "10001", "10010", "10100"]

def generate_bar_code(input_code):
    processed_code = input_code.replace("-", "")
    sum = 0
    # generate checksum
    for character in processed_code:
        sum += int(character)
    checksum = 10 - (sum % 10)
    processed_code += str(checksum)
    
    # use code lookup table to format the binary representation of the barcode
    binary = "1"
    for number in processed_code:
        binary += codes[int(number)]
    binary += "1"
    draw_bar_code(binary)

def draw_bar_code(input_code):
    # set the turtle window to top
    wn = Screen()
    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    pen = Turtle()
    pen.hideturtle()
    pen.speed("fastest")
    width = len(input_code) * 10 + 10
    xCor = -width / 2

    # draw a box to surround the bar code
    pen.pensize(5)
    pen.setheading(0)
    pen.up()
    pen.setpos(xCor - 10, -40)
    pen.down()
    pen.forward(width)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(80)

    # for each digit, draw either a short or long line, then move to the right
    pen.setheading(90)
    for digit in input_code:
        pen.up()
        pen.setpos(xCor, -25)
        pen.down()
        if(digit == "0"):
            pen.forward(25)
        elif(digit == "1"):
            pen.forward(50)
        xCor += 10

    wn.mainloop()

# TASK THREE OUTPUT:
# See pdf file



# Task selector
while(True):
    selection = int(
        input("Which task would you like to run? Type 1, 2, or 3. Type 0 to quit: "))
    if (selection == 0):
        quit()
    if (selection == 1):
        task_one_main()
    elif (selection == 2):
        task_two_main()
    elif (selection == 3):
        task_three_main()
    print()