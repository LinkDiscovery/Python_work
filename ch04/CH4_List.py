for value in range (6):
    print(value)
    
numbers = list(range(1,10,2))
print(numbers)

num = set(range(1,6))
print(num)


squares = []
for value in range(1,11):
    # square = value ** 2
    squares.append(value**2)
    
print(squares)
print(value)

# java와 다르게 for 문이 끝났어도 value 값은 존재한다.

squares = [value **2 for value in range(1,11)]
print(squares)

print(squares[0:3])#slice index 상 0,1,2가 출력됌 
print(squares[:4]) # 0부터 4까지
print(squares[-3:])#list 크기와 상관없이 뒤에서 3개 값 출력
print(squares[:-3])# 뒤에서 3개 값 빼고 출력 
# list를 만드는데 for문으로 만드는 것이 리스트 내포라 이해해라 일단 
# simple coding

# list  slice ** slice 가 계속해서 나옴 중요 


a = [1,2]
b = [3,4]

c= a+b
print(c)
a=[1,2,3,4]
b=[3,4]
c1=[x for x in a if x not in b]
c2 = list(set(a)-set(b))
print(c1)
print(c2)
# list에 빼기는 없음 .
matrix = [[3,7,9],
          [4,5,6],
          [8,10,1]]
print(matrix[2][2])


a= [10,20,30,40,50]
b=a ### shallow copy
b = a[0:3]### deep copy
a[0] = 100
print(b)

a = [[1,2,3,],[4,5,6]]
b = a[:] #shallow copy
print(b) #[[1,2,3,],[4,5,6]]
a[0][0] = 100
print(b)

players = ['charles','martina','michael','florence','eli']
for player in players[:3] :
    print(player.title())

my_foods = ['pizza', 'falafel','carrot cake']
friend_foods = my_foods[:]#deep copy 형식으로 된 것 , 데이터가 따라 바뀌진않음 , 데이터를 복사함
# friend_foods = my_foods shallow copy 데이터가 따라 바뀜, 데이터말고 주소를 복사함 
my_foods.append('cannoli')
print(my_foods)
print(friend_foods)

dimensions = (10,20,30,40,50)

print(dimensions)
for dimension in dimensions :
    print(dimension)

dimensions = (200,50)







