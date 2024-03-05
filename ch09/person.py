class Person:
    def __init__(self, name, age, address):
        """"""
        self.name = name
        self.age = age
        self.address = address
        self.weight2 = [1,2,3,4,5,6,7] #공개속성 
        self.weight = 70
        self.height = 170
        self.__vision = 1.0 # private 속성
        
    def __call__(self):
        return self.weight / (self.height**2)
        
    def __len__(self):
        return len(self.weight2)

    def __str__(self): ## 용도 Person은 객체 , 객체 출력시 필요한 것은 스트링 , 스트링을 만들어주는 함수를 정의
        return "{}\t{}\t{}".format(self.name,self.age,self.address)
    
    def __eq__(self,other):
        return self.address == other.address
    

    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))
        
        
        
new_person = Person('hong',20,'마산')
other_person = Person('shin',30,'마산')
print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight2}")
# print(f"시력은 {new_person.__vision}")
# print("시력은 {}".format(new_person.__vision))  
new_person.show_person_vision()


print(str(new_person))
print(new_person.__str__())
print(new_person)
#print(str(new_person))
# print(new_person.__str__())
# print(new_person)
# 위 세가지 전부 같은 값을 나타냄

# print(new_person) - 아무것도 설정 안했을 때 
# print는 스트롱으로 값을 나타낸다. 

my_list=[1,2,3,4]
print(len(new_person))
print(new_person.__len__())
a = "아야어요으이"
print(len(a))

print(new_person == other_person)

print(f"체질량은 {new_person.__call__}") # 교수님은 new_person만 해도 이 값이 호출됨 
                                        # 나는 weight, height 를 안지우고 해서 그런 것인가? 
                                         # new_person만 해도 호출되는 경우가 어떤 경우인지 ... 















