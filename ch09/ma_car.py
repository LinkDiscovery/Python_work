from car import Car
    # file      class

my_new_car = Car('audi','a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading =23 # 속성이 public 이다. 
my_new_car.read_odometer()
my_new_car.update_odometer(111)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()