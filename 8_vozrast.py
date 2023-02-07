from itertools import product
cnt=0
for i in product('0123456789ABCDEF', repeat=5):
	a="".join(i)
	if a[0]!='0' and a[0]<=a[1]<=a[2]<=a[3]<=a[4]:
		cnt+=1
print(cnt)