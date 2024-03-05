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
    
class Battery:
    """배터리"""
    def __init__(self,battery_size=00):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"차량 배터리 크기는 {self.battery_size}")

    def get_range(self):
        if self.battery_size <= 40:
            range = 150
        elif self.battery_size >= 65:
            range = 225
        print(range)
        
class ElectricCar(Car):
    """전기차"""
    def __init__(self, make,model,year, large_battery=Battery()):
        super().__init__(make,model,year)
        self.battery = large_battery

    def describe_battery(self):
        return(f"이차 배터리 용량은 {self.battery.battery_size}")
    
    def get_descriptive_name(self):
        print(super().get_descriptive_name())
        print(f"차량 배터리 크기는 {self.battery.battery_size}")

