"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
# Define bonus default as 0, "" works but it would be a string so it might cause trouble in the future
bonus = 0

# When sales value is greater than 0 run the if statement
while sales >= 0:
    # When sales amount is below 1000 multiple it by 0.1 which is 10%
    if sales < 1000:
        bonus = sales * 0.1
    # When sales amount is or above 1000 multiple it by 0.15 which is 15% and save the value as bonus
    elif sales >= 1000:
        bonus = sales * 0.15
    # Tell user the value then ask them to key in the value again, it will only stop when the first statement is false
    print("Your bonus is: $", bonus)
    sales = float(input("Enter sales: $"))
