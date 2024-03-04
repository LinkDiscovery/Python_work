class Car:
    
    """자동차 클래스 """
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=00
        
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """자동차 주행거리 출력"""
        print(f"Thin car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
        """주행거리 입력값"""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
        else :
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘립니다"""
        self.odometer_reading += miles
            
class Battery:
    """전기차의 배터리를 표현"""
    
    def __init__(self,battrey_size=40):
        """배터리 속성 초기화"""
        self.battery_size = battrey_size
        
    def describe_battery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print(f"This car has a {self.battery_size}-kWh battery.")    
            
            
class ElectricCar(Car):
    """전기차"""
    def __init__(self,make,model,year, large_battery=Battery()): #defalut parameter/ large_battery=Battery() / 자주 쓰임
        super().__init__(make,model,year)
        self.battery_size = large_battery # 속성 추가 방법
        
    def describe_battery(self):
        return print(f"이차의 배터리 용량은 {self.battery.battery_size}")    
    
    def get_descriptive_name(self):
        print(super().get_descriptive_name())
        self.battery = Battery()
        print(f"차량 배터리 크기는 {self.battery.battery_size}")
    
my_leaf = ElectricCar('nissan','leaf',2024,3000)
print(my_leaf.get_descriptive_name())
print(f"이차 배터리 용량은 {my_leaf.battery_size}\n")
my_leaf.get_descriptive_name()

my_car = Car('Bentz','E200',2023)
print(f"차 제원은 {my_car.get_descriptive_name()}")
my_leaf.battery.describe_battery()

large_battery = Battery(80)
large_battery_car = ElectricCar('nissan','leaf',2024, large_battery)

large_battery_car.battery_size.describe_battery()