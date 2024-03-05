class Person:
    def __init__(self, name, age, address):
        """"""
        self.name = name
        self.age = age
        self.address = address
        self.weight = [65,80,23,56] #공개속성 
        self.height = 170
        self.__vision = 1.0 # private 속성
    
    
    def __getitem__(self, indx):
        return self.weight[indx]

    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))
        
        
        
new_person = Person('hong',20,'마산')
other_person = Person('shin',30,'마산')
print(f"현재 체중은 {new_person[2]}")
