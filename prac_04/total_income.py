def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    # Make it a global var so it can be used in the report_printing function
    global number_of_months
    number_of_months = int(input("How many number of months? "))
    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    report_printing(incomes)


def report_printing(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(number_of_months):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
