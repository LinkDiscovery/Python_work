from car import ElectricCar

my_leaf = ElectricCar('nissan','leaf',2024)
print(f"전기차는 {my_leaf.get_descriptive_name()}")
print("전기차는 {}".format(my_leaf.get_descriptive_name())) # {} 안에 들어가는 내용을 format안에 있는 걸로 대체한다.
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
