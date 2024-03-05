class Shape:
    
    def __init__(self,base,height):
        self.__base = base
        self.__height = height # private 변수 
        
    
    @property #decorator for getter # 
    def get_base(self):
        return self.__base

    @property #decorator for getter # 
    def get_height(self):      # get_height는 읽기만 하는 함수다
        return self.__height

    @height.setter # 변경만 하는 함수다 
    def height(self,value):
        self.height = value

###
    def get_data():
        return 1,2,3

    _,a,b = get_data()
    print(get_data())
#get_data는 세개를 리턴하는데 _에 꺼는 빼고 리턴하겠다 라는 의미 

a = [1,2,3]
b = [11,22,33]
mylist = [*a,*b] ### 병합
print(mylist)
c=['a','b']
z=zip(a,c)
print(list(z)) #a와 b 배열 순서대로 짝을 맞춰서 출력, 짧은 길이에 맞춰서 출력함 
z=zip(a,b)
print(list(z))

## getter, setter 를 정의하는데 decorator 사용 


