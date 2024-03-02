def test():
    return(10,20)

a,b = test()#tuple 값을 리턴하였음
print(f"a={a},b={b}")
print(type(a))
lis = ['a','b','c','d']
for i, value in enumerate(lis):# 함수가 튜플을 리턴한다.
    print(f"i={i},value={value}")
#  --------------------------------------
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# 무한루프입니다.
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name =='q':
    

    
# ------------------------------------------------210p

def modify_string(s):
    s = "world"
    
st = "hello"

modify_string(st)
print(st)