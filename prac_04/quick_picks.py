import random

pick_number = int(input("How many quick picks? "))

# loop the amount of time entered in input
for i in range(pick_number):
    # sets result to an empty one every loop
    result = []
    # loop 6 times and generate number within the range of 1 to 45
    for i in range(6):
        numbers = (random.randrange(1, 45))
        result.append(numbers)
        result.sort()
    # print the result of the inner for loop
    print(result)
