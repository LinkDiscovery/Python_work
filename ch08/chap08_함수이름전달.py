# 함수의 매개변수로 함수 전달하기

def ten_times(func):
    for i in range(5):
        func()
        
def print_hello():
    print("hello")
    
ten_times(print_hello)

def print_work():
    print('coding')
    
ten_times(print_work)
    #----------------------------------------------------------------------
def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def apply_operation(operation, x, y):
    return operation(x,y)

result = apply_operation(add, 3,4)
result2 = apply_operation(minus, 3,4)

print(result)
print(result2)