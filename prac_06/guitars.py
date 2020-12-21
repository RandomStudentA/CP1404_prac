from prac_06.guitar import GuitarAttributes

guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    if year > 2020:
        print("That's the future")
    else:
        cost = input("Cost: $")
        add_guitar = GuitarAttributes(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")
else:
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>1} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
