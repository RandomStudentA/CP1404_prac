Year = 2020

class GuitarAttributes:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return Year - self.year

    def is_vintage(self):
        return self.get_age() > 49


Guitar = GuitarAttributes("Gibson L-5 CES", 1922, 16035.40)
Not_Vintage_Guitar = GuitarAttributes("Not_Vintage_Guitar", 2019, 16035.40)

print("{} age {}, Expected year 98".format(Guitar.name, Guitar.get_age()))
print("{} age {}, Expected year 1".format(Not_Vintage_Guitar.name, Not_Vintage_Guitar.get_age()))
print("{} age {}, Expected True".format(Guitar.name, Guitar.is_vintage()))
print("{} age {}, Expected False".format(Not_Vintage_Guitar.name, Not_Vintage_Guitar.is_vintage()))