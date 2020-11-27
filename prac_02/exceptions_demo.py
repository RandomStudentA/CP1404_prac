"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 ANS: When the item is not an integer
2. When will a ZeroDivisionError occur?
ANS: When the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # if the denominator is 0 it will prompt thus not triggered the ZeroDivisionError
    if denominator == 0:
        print('Denominator cannot be 0')
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")