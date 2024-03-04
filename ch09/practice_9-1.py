class Restaurant : 
    def __init__(self,name,type):
        """name과 age 속성 초기화"""
        self.restaurant_name=name
        self.cuisine_type=type
        
    def describe_restaurant(self):
        print(f"이름:{Restaurant_obj.restaurant_name} 타입:{Restaurant_obj.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name}의 문이 열려있습니다.")
    
Restaurant_obj = Restaurant('공화춘 ', '중식')
Restaurant_obj.describe_restaurant()
Restaurant_obj.open_restaurant()

Restaurant_obj2 = Restaurant("스시", "일식")
Restaurant_obj2.describe_restaurant()
Restaurant_obj2.open_restaurant()

