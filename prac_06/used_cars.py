from prac_06.car import Car


def main():
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)

    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print("Limo {}, {}".format(limo.fuel, limo.odometer))
    print("Limo {self.fuel}, {self.odometer}".format(self=limo))

main()