from decimal import Decimal

# Ask user to input number of items
number_of_items = int(input(" Number of items: "))
# Set total price to 0
total_price = 0

# As long as the inputted number is below 0 it will keep looping
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input(" Number of items: "))
# Every price will be added to total price in this loop
for i in range(number_of_items):
    price = float(input("Price of items: $"))
    total_price += price
# When total price is above 100 it will be reduced to 90% of what it was
if total_price > 100:
    total_price *= 0.9
    total_price = round(total_price, 2)
    print("Total price for ", number_of_items, "is", total_price)
