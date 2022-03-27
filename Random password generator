import random
import string

set_char_upper = ""
set_char_lower = ""
set_char_number = ""
set_char_special = ""

def set_characters():

    global set_char_upper, set_char_lower, set_char_number, set_char_special

    while set_char_upper.isdigit() == False:
        set_char_upper = input("Choose how many upper case characters you want")
        if set_char_upper.isdigit() == False:
            print("That is not a number!")
        else:
            break

    while set_char_lower.isdigit() == False:
        set_char_lower = input("Choose how many lower case characters you want")
        if set_char_lower.isdigit() == False:
            print("That is not a number!")
        else:
            break

    while set_char_number.isdigit() == False:
        set_char_number = input("Choose how many number character you want")
        if set_char_number.isdigit() == False:
            print("That is not a number!")
        else:
            break

    while set_char_special.isdigit() == False:
        set_char_special = input("Choose how many special characters you want")
        if set_char_special.isdigit() == False:
            print("That is not a number!")
        else:
            break

def create_password():

    global set_char_upper, set_char_lower, set_char_number, set_char_special

    upper_char = ''.join([random.choice(string.ascii_uppercase) for i in range(int(set_char_upper))])

    lower_char = ''.join([random.choice(string.ascii_lowercase) for i in range(int(set_char_lower))])

    number_char = [random.randint(0,9) for i in range(int(set_char_number))]
    number_char_to_string = int(''.join(map(str, number_char)))

    special_char = ''.join([random.choice(string.punctuation) for i in range(int(set_char_special))])

    password_maker = ''.join(upper_char + lower_char + str(number_char_to_string) + special_char)
    password_maker_shuffle = ''.join(random.sample(password_maker, len(password_maker)))

    # return print(upper_char, lower_char, number_char_to_string, special_char)
    return print(password_maker_shuffle)

set_characters()
create_password()

if __name__ == '__main__':
    pass


