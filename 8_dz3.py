from itertools import product
cnt = 0
for i in product('0123456', repeat = 7):
	a=''.join(i)
	if a[0]!='3' and a[0]!='5' and a[0]!='0' and not('22' in a and '44' in a):
		cnt+=1
print(cnt)