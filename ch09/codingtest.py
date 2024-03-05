a=123
b=123

print(a*(b%10))
print(a*((b-(b%10))%10))
print(a*(b-(b-(b%10))%10))
print(a*b)