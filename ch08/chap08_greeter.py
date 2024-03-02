def greet_user(username): #이거 다음에 쓰여진 것은 전부 바디이다.
                          # username은 스트링은 immutable
    """인사말"""#docstring  주석
    print(f"hello, {username.title()}")
    username = 'kim'

input_name = 'jesse'
greet_user(input_name)
input_name = 'kim'
greet_user(input_name) # 함수 호출
 
 
 
help(greet_user) # 
print(greet_user.__doc__)#docstring  출력

def describe_pet(animal_type, pet_name):#defalut parameter
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
describe_pet('dog','willie')

describe_pet(animal_type='hamster',pet_name='harry')








