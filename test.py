# a= {1:"A+",
#     2:"b+",
#     3:"c+"}

# for a1 in a : 
#     print(a[a1])

# b = {
# 	3:'b+',
#     6:'a+',
#     9:'s+'
# }
# print(b)
# b[3]

# first = lambda x : x[0]
# second = lambda x : x[1]

# for row in b.items():
# 	print(first(row), second(row))
 
# sorted(b.items(), key=lambda x:x[1])

a=0
b=30

c = (a*60)+b-45
hr = int(c/60)
mi = int(c%60)

if (a==0):
    a=24
    c = (a*60)+b-45
    hr = int(c/60)
    mi = int(c%60)

    print(f"{hr} {mi}") 

else:
    print(f"{hr} {mi}") 

