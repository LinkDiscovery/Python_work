class Car:
    """자동차 클래스 """
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
        
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
    
my_new_car = Car('audi','a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading =23 # 속성이 public 이다. 
my_new_car.read_odometer()
my_new_car.update_odometer(111)
my_new_car.read_odometer()
my_new_car.update_odometer(10)
my_new_car.read_odometer()
