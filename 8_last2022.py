from itertools import product

k = 0
for x in product('01234567', repeat=5):
	a = ''.join(x)
	if a.count('4') == 2 and a[0]!='0' and '14' not in a and '34' not in a and '54' not in a and '74' not in a and '41' not in a \
	and '43' not in a and '45' not in a and '47' not in a:
		k+=1
print(k)

