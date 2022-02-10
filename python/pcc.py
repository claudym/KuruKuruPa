from car import Car, ElectricCar

ore_no_tesla = ElectricCar('tesla', 'model x', 2019)
print(ore_no_tesla.get_descriptive_name())

ore_no_tesla.odometer = 50
ore_no_tesla.read_odometer()

ore_no_tesla.battery.describe_battery()
ore_no_tesla.battery.get_range()