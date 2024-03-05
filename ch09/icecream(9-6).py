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

class IceCreamStand(Restaurant):
    
    def __init__(self,name,type, flavors):
        """ """
        super().__init__(name,type)
        self.flavors = flavors
    
    def show_flavors(self):
        print(f"아이스크림 맛은 {}입니다.".format(self.flavors)) #deep러닝에서 format 을 많이 사용함
       #  print(f"아이스크림 맛은 '{self.flavors}'입니다.") 위랑 같음
new_rest = Restaurant()
ice_cream = IceCreamStand('이태리','피자','매운맛')
ice_cream.show_flavors()
    
    
    
    
    
    
    
    
    
