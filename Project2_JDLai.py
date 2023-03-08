# Name: Joshua Lai
# Project 2
# Completed 3/7/2022

import time

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
    print("Your sentence encrypted is: ", encrypted)
    print("Your sentence decryped is: ", decrypted)
    return
    

def get_num_of_characters(input_string):
    return len(input_string)
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

#task_one_main()

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

task_two_main()