import re

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = r"[!@#$%^&*()_-=+`~,./'[]<>?{}|\\]"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    # Make sure the length requirement is met
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    # Check for if a all the way to z is not inside, if its not it will be false triggering line 19
    elif not re.search("[a-z]", password):
        return False
    # Checking for capital letters from A to Z
    elif not re.search("[A-Z]", password):
        return False
    # Checking for numbers 0 to 9
    elif not re.search("[0-9]", password):
        return False
    # If predefined special characters is inside, it will return true and skip the statement in line 18 due to boolean
    for character in SPECIAL_CHARACTERS:
        if character in password:
            return True
    # When it return false it will stay in while loop and execute the codes in it, if true it will skip the while loop
    return False


main()
