bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3].title())
print(bicycles[-1])
print(bicycles[-2])
message=f'bicycles[0] was a {bicycles[0].title()}!!!'
print(message)

# 요소 수정 추가 제거 

# 요소 수정
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

motocycles[0]='ducati'
print(motocycles)

# 요소 추가
motocycles.append('honda')
print(motocycles)

# 요소 추가 2 insert 
motocycles.insert(1,'hundai')
print(motocycles)

# 요소 제거 
del motocycles[0]
print(motocycles)

popped_motor=motocycles.pop()
print(motocycles)
print(motocycles.pop())

motocycles = ['honda','bucati','yamaha','suzuki','bucati']
print(motocycles)
motocycles.remove('bucati')
print(motocycles)
motocycles.remove('bucati')
print(motocycles)

invitinglist = ['신건영', '김보성' , '홍길동', '윤석열']
print(invitinglist)

# list생성
a=list()
b=[]
print(type(a))