class Person:
    count = 0 # 클래스 변수 
    def __init__(self, name, age, address): # 생성자 역할 
        """"""
        self.name = name### 인스턴스 변수 
        self.age = age
        self.address = address
        self.weight = [65,80,23,56] #공개속성 
        self.height = 170
        self.__vision = 1.0 # private 속성
        print("{}객체가 생성됨".format(self.name))
        Person.count += 1
        
    def __getitem__(self, indx):
        return self.weight[indx]

    @classmethod # decorator - 자바 용어는 annotation
    def printing(cls):
        print("객체생성 {}".format(cls.count))

    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))
        
    def __del__(self):
        print("객체 {}이 소멸됨".format(self.name))
        
new_person = Person('hong',20,'마산')
other_person = Person('shin',30,'마산')
print(f"현재 체중은 {new_person[2]}")
print(new_person.age)
print(f"person 객체의 나이는{new_person.age:5}")
print("객체 타입은 {}".format(isinstance(new_person,Person)))
Person('guest', 11, 'jeju')
print(f"객체생성 {Person.count}")
print(new_person.count)
print(other_person.count)
Person.printing() ### 클래스 메소드 호출 
new_person.printing()
# 생성자로 만들어졌지만 참조 변수가 없으므로 , 바로 삭제되어버림?

## 프로그램이 종료되면 자동으로 garbage collection > 자바에서 사용되지 않는 객체들을 자동으로 수거하는 개념  
## __del__ 메서드는 프로그램이 종료되면 
## 여기서 실행 시켜보면 
## guest 객체는 생성되자 마자 삭제되지만 바로 삭제된다. 참조변수가 없기 때문에 , garbage collection의 영향
## 근데 다른 객체의 경우 모든 프로그램이 끝나고 소멸됨

## del 을 설정해놔서 사라지는건가? 아니면 원래 없어지는 걸 출력으로 나타내는 것인가? 
## 생성자가 소멸하기 전에 무엇인가를 실행시키기 위해 del 을 활용한다 . 소멸 직전에 호출 및 실행 

