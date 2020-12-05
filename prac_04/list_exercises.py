numbers = []
for i in range(5):
    number = int(input("Number "))
    numbers.append(number)
# Count start with 0 so 0 is the first number, and 4 is the last count in 5 numbers
print("The first number is " + str(numbers[0]))
print("The last number is " + str(numbers[4]))
# min finds the smallest int
print("The smallest number is " + str((min(numbers))))
# man finds the largest int
print("The largest number is " + str((max(numbers))))
# sum adds them together and then /5 is divided by 5
print("The average of the numbers is " + str((sum(numbers) / 5)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
enter_username = (input('Enter User name: '))
# When entered username matches completely with one of the string in usernames it will print access granted
if enter_username in (usernames):
    print("Access granted")
else:
    print("Access denied")
