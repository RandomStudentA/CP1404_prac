from taxi import Taxi

def main():


    taxi = Taxi('prius_1', 100 )
    taxi.drive(40)

    print('The, {self.name}, has {self.fuel} litters of fuel'.format(self = taxi), ',Fare Costs ${:.2f}'.format(taxi.get_fare()))


main()