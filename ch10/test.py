# with open('test.txt', encoding='utf-8') as file:
#     for line in file: # 줄바꿈 enter까지 다 읽는다.
#         print(line, end='')#restrip() 도 띄어쓰기나 필요없는거 삭제해준다.
# print('a',end='')#print 하면 뒤에 end='\n'이 defalt값임
# print('b',end='')

# def add(a,b):
#     return a+b
import csv

with open('grade.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)