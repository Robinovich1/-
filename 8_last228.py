from itertools import product

k = 0

for x in product('ГЕКЭ023', repeat=4):
	a = ''.join(x)
	k+=1
	if (a[0] == '0' or a[0] == '2' or a[0] == '3') and a[0]!= a[1] and a[1]!= a[2] and a[2]!= a[3]:
		print(k, a)