"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

# This is a try,except,else way to do it doesn't make use of boolean so "not" and "false" is pointless
finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer : "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        print("Valid result is:", result)
        exit()

# This is what is expected
finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter an integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

