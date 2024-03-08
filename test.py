a=21
b=16

c = (a*60)+b-45
hr = int(c/60)
mi = int(c%60)

if a <= 0 :
    a += 24
    c = (a*60)+b-45
    hr = int(c/60)
    mi = int(c%60)
    print(hr, mi) 
else : 
	print(hr,mi)