from itertools import product

k = 0
for x in product('ЛЕТО', repeat=4):
	a = ''.join(x)
	if a[0] == 'Л' or a[0] == 'Т':
		k+=1
print(k)
