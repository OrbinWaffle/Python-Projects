# Name: Joshua Lai
# Project 2
# Completed 3/7/2022

def main():
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

main()