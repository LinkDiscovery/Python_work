class Dog:
    """개 클래스"""
    
    def __init__(self,name,age): # self는 뭐냐?
        self.name = name  # 속성 > 자바의 클래스 field
        self.age = age
        self.__price = 100
        
    def sit(self):
        print(f"{self.name} is 앉기")
        
my_dog = Dog('Willie',6) # 생성자 호출 > 인스턴스 생성 > __init__() 함수가 자동 호출
                         # __ 특별의미 자동 호출
                         # name, age는 알겠는데 self는 뭐냐? 생성된 객체 > 자기자신
                         # 클래스의 모든 함수는 self를 포함해야한다.
                         # p.showDate(); p > receiver object , showData > 메소드, 메세지 
                         # p가 가리키는 객체에 메시지를 전달 한다. 
my_dog.sit() # self가 가리키는 것은 my_dog , 자바로 치면 수신객체 receiver object를 가리킨다. 
             # 생성자에서의 self는 객체를 가리키고 함수에서의 self는 ... 229p
             # self는 전달된다고하는데 눈에 보이는 전달은 없음 
# 다른 객체 만들기 
your_dog = Dog('Lucy',3)
your_dog.sit()
print(f"너의 강아지는 {your_dog.name}")
             
print(f"개이름은 {my_dog.name}")
             
             