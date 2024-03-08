# import os

# from pathlib import Path #리눅스 윈도우 맥 을 돌아가면서 쓰다보면 Path 문제가 많이 생긴다 
# # 서버는 다 리눅스 , 윈도우 서버는 잘 안쓴다. 비싸서 

# path = Path ('./aaa/aaa.txt')
# print(aaa)



a= 'shin kyun young'

for b in a :
    print(b)
    #공백을 기준으로 나누는 것 
    
a=0
b=43

c = (a*60)+b-45
hr = int(c/60)
mi = int(c%60)

if a == 0 :
    a=24
    c = (a*60)+b-45
    hr = int(c/60)
    mi = int(c%60)
    print(f"{hr} {mi}") 
else : 
	print(f"{hr} {mi}")