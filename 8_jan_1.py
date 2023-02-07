from itertools import product

k = 0
for x in product('polygn', repeat=5):
	a = ''.join(x)
	if a[0] == a[-1] and a[1] == a[-2] and (a[2] == 'o' or a[2] == 'y'):
		k+=1
print(k)