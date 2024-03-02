def modify_string(s):
    ### immutable 변수는 튜플, 숫자, 스트링, 불리언 
    s = s + "world"
    print(s)
st = "hello"
modify_string(st)
print(st)